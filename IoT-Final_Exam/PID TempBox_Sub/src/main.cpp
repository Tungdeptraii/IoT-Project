#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <LiquidCrystal_I2C.h>
#include "secrets/wifi.h"  
#include "secrets/mqtt.h"  
#include "ca_cert_hivemq.h"  


WiFiClientSecure tlsClient;
PubSubClient mqttClient(tlsClient);

LiquidCrystal_I2C lcd(0x27, 16, 2);

// MQTT Topics
const char *temperature_1_topic = "home/temperature_1";
const char *temperature_2_topic = "home/temperature_2";
const char *humidity_topic = "home/humidity";
const char *setpoint_topic = "home/setpoint";

float Setpoint = 0.0, PV1 = 0.0, PV2 = 0.0, Humidity = 0.0;

void displayLCD(float setpoint, float pv1, float pv2, float humidity);

void setup_wifi() {
    WiFi.begin(WiFiSecrets::ssid, WiFiSecrets::pass);
    while (WiFi.status() != WL_CONNECTED) {
        delay(100);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("WiFi connected");
}

void mqttCallback(char *topic, uint8_t *payload, unsigned int length) {
    payload[length] = '\0';  // Ensure null-terminated payload
    String message = String((char *)payload);

    if (strcmp(topic, temperature_1_topic) == 0) {
        PV1 = message.toFloat();
    } else if (strcmp(topic, temperature_2_topic) == 0) {
        PV2 = message.toFloat();
    } else if (strcmp(topic, humidity_topic) == 0) {
        Humidity = message.toFloat();
    } else if (strcmp(topic, setpoint_topic) == 0) {
        Setpoint = message.toFloat();
    }


    displayLCD(Setpoint, PV1, PV2, Humidity);
}

void displayLCD(float setpoint, float pv1, float pv2, float humidity) {

    lcd.setCursor(3, 0);
    lcd.print(setpoint, 1); 
    lcd.setCursor(12, 0);
    lcd.print(pv1, 1);       

    lcd.setCursor(3, 1);
    lcd.print(humidity, 1);  
    lcd.setCursor(12, 1);
    lcd.print(pv2, 1);       
}

void reconnectMQTT() {
    while (!mqttClient.connected()) {
        Serial.print("Attempting MQTT connection...");
        if (mqttClient.connect("esp32-subscriber", HiveMQ::username, HiveMQ::password)) {
            Serial.println("connected");
            mqttClient.subscribe(temperature_1_topic);
            mqttClient.subscribe(temperature_2_topic);
            mqttClient.subscribe(humidity_topic);
            mqttClient.subscribe(setpoint_topic);
        } else {
            Serial.print("failed, rc=");
            Serial.println(mqttClient.state());
            delay(2000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    setup_wifi();

    tlsClient.setCACert(ca_cert);
    mqttClient.setServer(HiveMQ::broker, HiveMQ::port);
    mqttClient.setCallback(mqttCallback);

    // Initialize LCD
    lcd.init();
    lcd.backlight();
    lcd.clear();

    lcd.setCursor(0, 0);
    lcd.print("SP:");
    lcd.setCursor(8, 0);
    lcd.print("PV1:");

    lcd.setCursor(1, 1);
    lcd.print("H:");
    lcd.setCursor(8, 1);
    lcd.print("PV2:");


    displayLCD(Setpoint, PV1, PV2, Humidity);
}

void loop() {
    if (!mqttClient.connected()) {
        reconnectMQTT();
    }
    mqttClient.loop();
}
