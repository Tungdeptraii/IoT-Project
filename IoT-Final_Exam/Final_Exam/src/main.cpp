#include <Wire.h>
#include <PID_v1.h>
#include <SPI.h>
#include <Adafruit_ADS1X15.h>
#include <SimpleKalmanFilter.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include "secrets/wifi.h"  // WiFi credentials
#include "secrets/mqtt.h"  // MQTT broker credentials
#include "ca_cert_hivemq.h"  // Certificate for secure MQTT connection

SimpleKalmanFilter kalman_1(2, 2, 0.02);
SimpleKalmanFilter kalman_2(2, 2, 0.05);

#define PIN_INPUT A0
#define PIN_OUTPUT 18 // Pin output for PWM control

Adafruit_ADS1115 ads;
WiFiClientSecure tlsClient;
PubSubClient mqttClient(tlsClient);

const int BUFFER_SIZE = 256;
char receivedMessage[BUFFER_SIZE];
bool newPIDValues = false;

// MQTT Topics
const char *temperature_1_topic = "home/temperature_1";
const char *temperature_2_topic = "home/temperature_2";
const char *kp_set_topic = "home/kp/set";
const char *ki_set_topic = "home/ki/set";
const char *kd_set_topic = "home/kd/set";
const char *setpoint_set_topic = "home/setpoint/set";
const char *kp_topic = "home/kp";
const char *ki_topic = "home/ki";
const char *kd_topic = "home/kd";
const char *setpoint_topic = "home/setpoint";
const char *pwm_topic = "home/pwm";
const char *time_topic = "home/time";

// PID Control
const float adc_ref_voltage = 4.096;
const int16_t adc_max_value = 32767;
const float mv_per_degree = 10.0;

double Setpoint = 19, Input, Output, temp;
double Kp = 72.975;
double Ki = 0.6954;
double Kd = 1940;
PID myPID(&Input, &Output, &Setpoint, Kp, Ki, Kd, REVERSE);

unsigned long previousPIDMillis = 0;
unsigned long previousMQTTMillis = 0;
const unsigned long PID_INTERVAL = 5; // Interval for PID computation in milliseconds
const unsigned long MQTT_INTERVAL = 1000; // Interval for MQTT publishing in milliseconds

void setup_wifi() {
    WiFi.begin(WiFiSecrets::ssid, WiFiSecrets::pass);
    while (WiFi.status() != WL_CONNECTED) {
        delay(100);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("WiFi connected");
}

float readTemperature(int channel) {
    int16_t adc_value = ads.readADC_SingleEnded(channel);
    if (adc_value < 0) {
        Serial.print("Failed to read from ADS1115 (Channel ");
        Serial.print(channel);
        Serial.println(")!");
        return NAN;
    }
    float voltage = (adc_value * adc_ref_voltage) / adc_max_value;
    return voltage * 1000.0 / mv_per_degree; // Convert voltage to temperature
}

void processMessage(const char *message) {
    if (strncmp(message, "SETPOINT-", 9) == 0) {
        Setpoint = atof(message + 9);
    } else if (strncmp(message, "Kp-", 3) == 0) {
        Kp = atof(message + 3);
        newPIDValues = true;
    } else if (strncmp(message, "Ki-", 3) == 0) {
        Ki = atof(message + 3);
        newPIDValues = true;
    } else if (strncmp(message, "Kd-", 3) == 0) {
        Kd = atof(message + 3);
        newPIDValues = true;
    }
}

void mqttCallback(char *topic, uint8_t *payload, unsigned int length) {
    payload[length] = '\0'; // Null-terminate the string
    String message = String((char *)payload);

    if (strcmp(topic, kp_set_topic) == 0) {
        Kp = message.toFloat();
        newPIDValues = true;
        Serial.println("Kp updated from MQTT");
    } else if (strcmp(topic, ki_set_topic) == 0) {
        Ki = message.toFloat();
        newPIDValues = true;
        Serial.println("Ki updated from MQTT");
    } else if (strcmp(topic, kd_set_topic) == 0) {
        Kd = message.toFloat();
        newPIDValues = true;
        Serial.println("Kd updated from MQTT");
    } else if (strcmp(topic, setpoint_set_topic) == 0) {
        Setpoint = message.toFloat();
        Serial.println("Setpoint updated from MQTT");
    }
}

void setup() {
    Serial.begin(115200);
    delay(10);
    setup_wifi();

    tlsClient.setCACert(ca_cert);  // Use the MQTT broker's certificate for secure connection

    mqttClient.setCallback(mqttCallback);
    mqttClient.setServer(HiveMQ::broker, HiveMQ::port);  // Set MQTT server details

    if (!ads.begin()) {
        Serial.println("Failed to initialize ADS1115!");
    }
    ads.setGain(GAIN_TWOTHIRDS);  // Configure ADC gain

    myPID.SetMode(AUTOMATIC); // Start the PID controller
    myPID.SetTunings(Kp, Ki, Kd);
    myPID.SetOutputLimits(0, 255);

    pinMode(PIN_OUTPUT, OUTPUT);  // Set PIN_OUTPUT as an output for PWM control

    // Subscribe to topics
    mqttClient.subscribe(kp_set_topic);
    mqttClient.subscribe(ki_set_topic);
    mqttClient.subscribe(kd_set_topic);
    mqttClient.subscribe(setpoint_set_topic);
}

void SensorReadAndComputePID() {
    Input = kalman_1.updateEstimate(readTemperature(0));
    temp = readTemperature(1);

    if (isnan(Input) || isnan(temp)) {
        Serial.println("Failed to read sensor data!");
        return;
    }

    if (newPIDValues) {
        myPID.SetTunings(Kp, Ki, Kd);
        newPIDValues = false;
    }

    myPID.Compute();  // Compute the PID output
    analogWrite(PIN_OUTPUT, Output);  // PWM output

    Serial.print(Setpoint);
    Serial.print(",");
    Serial.print(Input);
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.println(Output);
}

void PublishMQTT() {
    mqttClient.publish(temperature_1_topic, String(Input).c_str(), false);
    mqttClient.publish(temperature_2_topic, String(temp).c_str(), false);

    mqttClient.publish(kp_topic, String(Kp).c_str(), false);
    mqttClient.publish(ki_topic, String(Ki).c_str(), false);
    mqttClient.publish(kd_topic, String(Kd).c_str(), false);
    mqttClient.publish(setpoint_topic, String(Setpoint).c_str(), false);
    mqttClient.publish(pwm_topic, String(Output).c_str(), false);
    mqttClient.publish(time_topic, String(millis()).c_str(), false); // Time in milliseconds
}

void UARTProcess() {
    if (Serial.available() > 0) {
        int bytesRead = Serial.readBytesUntil('\n', receivedMessage, BUFFER_SIZE - 1);
        if (bytesRead > 0) {
            receivedMessage[bytesRead] = '\0'; 
            processMessage(receivedMessage);
            memset(receivedMessage, 0, sizeof(receivedMessage));
        }
    }
}

void loop() {
    if (!mqttClient.connected()) {
        while (!mqttClient.connected()) {
            Serial.print("Attempting MQTT connection...");
            if (mqttClient.connect("esp32-client", HiveMQ::username, HiveMQ::password)) {
                Serial.println("connected");

                // Resubscribe to topics after reconnect
                mqttClient.subscribe(kp_set_topic);
                mqttClient.subscribe(ki_set_topic);
                mqttClient.subscribe(kd_set_topic);
                mqttClient.subscribe(setpoint_set_topic);
            } else {
                Serial.print("failed, rc=");
                Serial.print(mqttClient.state());
                delay(1000);
            }
        }
    }

    mqttClient.loop();  // Process incoming MQTT messages

    UARTProcess();  // Process UART messages

    unsigned long currentMillis = millis();

    if (currentMillis - previousPIDMillis >= PID_INTERVAL) {
        previousPIDMillis = currentMillis;
        SensorReadAndComputePID();
    }

    if (currentMillis - previousMQTTMillis >= MQTT_INTERVAL) {
        previousMQTTMillis = currentMillis;
        PublishMQTT();
    }
}
