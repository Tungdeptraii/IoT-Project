#include <Wire.h>
#include <PID_v1.h>
#include <SPI.h>
#include <Adafruit_ADS1X15.h>
#include <SimpleKalmanFilter.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <Ticker.h>
#include <DHT.h>
#include <LiquidCrystal_I2C.h>  // Include the LCD library
#include "secrets/wifi.h"  // WiFi credentials
#include "secrets/mqtt.h"  // MQTT broker credentials
#include "ca_cert_hivemq.h"  // Certificate for secure MQTT connection

SimpleKalmanFilter kalman_1(2, 2, 0.02);
SimpleKalmanFilter kalman_2(2, 2, 0.05);

#define PIN_INPUT A0
#define RELAY_PIN 26
#define PIN_OUTPUT 18 // Pin output for PWM control
#define DHTPIN 13     // Pin kết nối cảm biến DHT11
#define DHTTYPE DHT11 // Loại cảm biến DHT
namespace
{
    Adafruit_ADS1115 ads;
    DHT dht(DHTPIN, DHTTYPE);
    WiFiClientSecure tlsClient;
    PubSubClient mqttClient(tlsClient);
    Ticker PIDTicker;
    Ticker MQTTTicker;

    // Initialize LCD: (address, columns, rows)
    LiquidCrystal_I2C lcd(0x27, 16, 2); // Adjust the address and size as per your LCD

    const int BUFFER_SIZE = 256;
    char receivedMessage[BUFFER_SIZE];
    bool newPIDValues = false;

    // MQTT Topics
    const char *temperature_1_topic = "home/temperature_1";
    const char *temperature_2_topic = "home/temperature_2";
    const char *humidity_topic = "home/humidity"; // MQTT topic cho độ ẩm
    const char *kp_set_topic = "home/kp/set";
    const char *ki_set_topic = "home/ki/set";
    const char *kd_set_topic = "home/kd/set";
    const char *setpoint_set_topic = "home/setpoint/set";
    const char *kp_topic = "home/kp";
    const char *ki_topic = "home/ki";
    const char *kd_topic = "home/kd";
    const char *setpoint_topic = "home/setpoint";
    const char *pwm_topic = "home/pwm";
    const char *relay_control_topic = "home/relay";

    // PID Control
    const float adc_ref_voltage = 4.096;
    const int16_t adc_max_value = 32767;
    const float mv_per_degree = 10.0;

    double Setpoint = 19, Input, Output, temp, humidity;
    double Kp = 72.975;
    double Ki = 0.6954;
    double Kd = 1940;
    PID myPID(&Input, &Output, &Setpoint, Kp, Ki, Kd, REVERSE);
}

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
    payload[length] = '\0'; // Ensure null-terminated payload
    String command = String((char *)payload);
    command.trim(); // Remove leading/trailing spaces

    if (strcmp(topic, kp_set_topic) == 0) {
        Kp = command.toFloat();
        newPIDValues = true;
    } else if (strcmp(topic, ki_set_topic) == 0) {
        Ki = command.toFloat();
        newPIDValues = true;
    } else if (strcmp(topic, kd_set_topic) == 0) {
        Kd = command.toFloat();
        newPIDValues = true;
    } else if (strcmp(topic, setpoint_set_topic) == 0) {
        Setpoint = command.toFloat();
    } else if (strcmp(topic, relay_control_topic) == 0) {
        int relayState = command.toInt();
        if (relayState == 1) {
            digitalWrite(RELAY_PIN, LOW); // Relay ON
            Serial.println("Relay ON");
        } else if (relayState == 0) {
            digitalWrite(RELAY_PIN, HIGH); // Relay OFF
            Serial.println("Relay OFF");
        } else {
            Serial.println("Invalid command for relay control");
        }
    }
}

void SensorReadAndComputePID() {
    Input = kalman_1.updateEstimate(readTemperature(0)); // Read temperature from ADC
    temp = readTemperature(1);                          // Read temperature from another channel
    humidity = dht.readHumidity();                      // Read humidity from DHT11 sensor

    if (isnan(Input) || isnan(temp) || isnan(humidity)) { // Check for invalid sensor readings
        Serial.println("Failed to read sensor data!");
        return;
    }

    if (newPIDValues) { // Update PID values if changed
        myPID.SetTunings(Kp, Ki, Kd);
        newPIDValues = false;
    }

    myPID.Compute();  // Compute PID output
    analogWrite(PIN_OUTPUT, Output);  // Write PWM value to output pin

    // Display values on Serial
    Serial.print(Setpoint);
    Serial.print(",");
    Serial.print(Input);
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.println(Output);


 
}

void PublishMQTT() {
    mqttClient.publish(temperature_1_topic, String(Input).c_str(), false); // Temperature 1
    mqttClient.publish(temperature_2_topic, String(temp).c_str(), false); // Temperature 2
    mqttClient.publish(humidity_topic, String(humidity).c_str(), false); // Humidity
    mqttClient.publish(kp_topic, String(Kp).c_str(), false); // Kp value
    mqttClient.publish(ki_topic, String(Ki).c_str(), false); // Ki value
    mqttClient.publish(kd_topic, String(Kd).c_str(), false); // Kd value
    mqttClient.publish(setpoint_topic, String(Setpoint).c_str(), false); // Setpoint value
    mqttClient.publish(pwm_topic, String(Output).c_str(), false); // PWM value
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
void displayLCD(float setpoint, float pv1, float pv2, float humidity) {


    lcd.setCursor(0, 0); // Dòng đầu tiên
    lcd.print("SP:");
    lcd.print(setpoint, 1); // In SP_ với 1 chữ số thập phân
    lcd.print(" PV1:");
    lcd.print(pv1, 1); // In PV1_ với 1 chữ số thập phân

    lcd.setCursor(0, 1); 
    lcd.print("Hu:");
    lcd.print(humidity, 1);
    lcd.print(" PV2:");
    lcd.print(pv2, 1); 
}

void setup() {
    Serial.begin(115200);
    delay(10);
    setup_wifi();

    tlsClient.setCACert(ca_cert);  // Use the MQTT broker's certificate for secure connection

    mqttClient.setCallback(mqttCallback);
    mqttClient.setServer(HiveMQ::broker, HiveMQ::port);  // Set MQTT server details

    dht.begin(); // Initialize DHT11 sensor

    if (!ads.begin()) {
        Serial.println("Failed to initialize ADS1115!");
    }
    ads.setGain(GAIN_TWOTHIRDS);  // Configure ADC gain

    myPID.SetMode(AUTOMATIC); // Start the PID controller
    myPID.SetTunings(Kp, Ki, Kd);
    myPID.SetOutputLimits(0, 255);

    pinMode(PIN_OUTPUT, OUTPUT);  // Set PIN_OUTPUT as an output for PWM control
    pinMode(RELAY_PIN, OUTPUT);   // Set RELAY_PIN as an output
    digitalWrite(RELAY_PIN, HIGH);

    // Initialize the LCD
    lcd.init();
    lcd.setBacklight(true);  // Turn on the backlight
    lcd.clear();

    // Subscribe to topics
    mqttClient.subscribe(kp_set_topic);
    mqttClient.subscribe(ki_set_topic);
    mqttClient.subscribe(kd_set_topic);
    mqttClient.subscribe(setpoint_set_topic);
    mqttClient.subscribe(relay_control_topic);

    // Start tickers
    PIDTicker.attach_ms(5, SensorReadAndComputePID); // Run PID every 5ms
    MQTTTicker.attach_ms(1000, PublishMQTT);        // Publish MQTT every 1000ms
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
                mqttClient.subscribe(relay_control_topic);
            } else {
                Serial.print("failed, rc=");
                Serial.print(mqttClient.state());
                delay(1000);
            }
        }
    }

    mqttClient.loop();  // Process incoming MQTT messages
    UARTProcess();      // Process UART messages
    displayLCD(Setpoint, Input, temp, humidity);
}
