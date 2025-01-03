#include <Arduino.h>
#include "secrets/wifi.h"
#include "wifi_connect.h"
#include <WiFiClientSecure.h>
#include "ca_cert_hivemq.h"
#include "secrets/mqtt.h"
#include <PubSubClient.h>
#include "MQTT.h"
#include <Ticker.h>
#include <DHT.h>
#include <Adafruit_ADS1X15.h>
#include <LiquidCrystal_I2C.h> // LCD I2C library
#include <SPI.h>

#define DHT11PIN 13U
#define LED_PIN 15U
#define BUZZER_PIN 25U
#define RELAY_PIN 26U

namespace
{
    const char *ssid = WiFiSecrets::ssid;
    const char *password = WiFiSecrets::pass;
    const char *client_id = (String("esp32-client") + WiFi.macAddress()).c_str();

    DHT dht(DHT11PIN, DHT11);
    Adafruit_ADS1115 ads;
    LiquidCrystal_I2C lcd(0x27, 16, 2); // LCD I2C address 0x27, 16x2 display

    WiFiClientSecure tlsClient;
    PubSubClient mqttClient(tlsClient);

    Ticker SensorTicker;

    const char *temperature_topic = "home/temperature";
    const char *humidity_topic = "home/humidity";
    const char *temperature_1_topic = "home/temperature_1";
    const char *temperature_2_topic = "home/temperature_2";

    const char *set_temp_topic = "home/set_temp";
    const char *relay_control_topic = "home/relay_control";

    const float adc_ref_voltage = 4.096;
    const int16_t adc_max_value = 32767;
    const float mv_per_degree = 10.0;

    float set_temp = 29.0; 
    
}

float readTemperatureFromChannel(uint8_t channel)
{
    int16_t adc_value = ads.readADC_SingleEnded(channel);
    if (adc_value < 0)
    {
        Serial.print("Failed to read from ADS1115 (Channel ");
        Serial.print(channel);
        Serial.println(")!");
        return NAN;
    }

    float voltage = (adc_value * adc_ref_voltage) / adc_max_value; 
    return voltage * 1000.0 / mv_per_degree;
}

void updateLCD(float temp1, float temp2, float humidity)
{
    lcd.clear();
    lcd.setCursor(0, 0); 
    lcd.print("T1:");
    lcd.print(temp1, 1); 
    lcd.print(" H:");
    lcd.print(humidity, 1);
    lcd.print("%");
    lcd.setCursor(0, 1); 
    lcd.print("T2:");
    lcd.print(temp2, 1);
    
    
}

void SensorReadPublish()
{
    float temperature_1 = readTemperatureFromChannel(0);
    float temperature_2 = readTemperatureFromChannel(1);
    float humidity = dht.readHumidity();

    if (isnan(temperature_1) || isnan(temperature_2) || isnan(humidity))
    {
        Serial.println("Failed to read sensor data!");
        return;
    }

    Serial.print("Temperature_1: ");
    Serial.print(temperature_1);
    Serial.print("°C  ");
    Serial.print("Temperature_2: ");
    Serial.print(temperature_2);
    Serial.print("°C  ");
    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.println("%");

    updateLCD(temperature_1, temperature_2, humidity);

    if (temperature_1 > set_temp || temperature_2 > set_temp)
    {
        digitalWrite(BUZZER_PIN, HIGH); 
        Serial.println("Buzzer ON: One or more temperatures exceed threshold!");
    }
    else
    {
        digitalWrite(BUZZER_PIN, LOW); 
    }

    mqttClient.publish(humidity_topic, String(humidity).c_str(), false);
    mqttClient.publish(temperature_1_topic, String(temperature_1).c_str(), false);
    mqttClient.publish(temperature_2_topic, String(temperature_2).c_str(), false);
}

void mqttCallback(char *topic, uint8_t *payload, unsigned int length)
{
    if (strcmp(topic, set_temp_topic) == 0)
    {
        char setTempStr[length + 1];
        memcpy(setTempStr, payload, length);
        setTempStr[length] = '\0';
        float newSetTemp = atof(setTempStr);

        if (newSetTemp > 0) 
        {
            set_temp = newSetTemp;
            Serial.print("New set temperature: ");
            Serial.println(set_temp);

            mqttClient.publish(set_temp_topic, String(set_temp).c_str(), false);
        }
        else
        {
            Serial.println("Invalid set temperature received!");
        }
    }
    else if (strcmp(topic, relay_control_topic) == 0)
    {
        char command[length + 1];
        memcpy(command, payload, length);
        command[length] = '\0';

        if (strcmp(command, "ON") == 0)
        {
            digitalWrite(RELAY_PIN, HIGH); 
            Serial.println("Relay ON");
        }
        else if (strcmp(command, "OFF") == 0)
        {
            digitalWrite(RELAY_PIN, LOW); 
            Serial.println("Relay OFF");
        }
        else
        {
            Serial.println("Invalid relay command received!");
        }
    }
}

void setup()
{
    Serial.begin(115200);
    delay(10);
    setup_wifi(ssid, password);
    tlsClient.setCACert(ca_cert);

    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("Initializing...");

    pinMode(LED_PIN, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, HIGH);

    mqttClient.setCallback(mqttCallback);
    mqttClient.setServer(HiveMQ::broker, HiveMQ::port);

    if (!ads.begin())
    {
        Serial.println("Failed to initialize ADS1115!");
    }
    ads.setGain(GAIN_ONE);

    SensorTicker.attach(1, SensorReadPublish); 

    const char *topics[] = {set_temp_topic, relay_control_topic};
    for (int i = 0; i < 2; i++)
    {
        mqttClient.subscribe(topics[i]);
    }
}

void loop()
{
    const char *topics[] = {set_temp_topic, relay_control_topic};
    MQTT::reconnect(mqttClient, client_id, HiveMQ::username, HiveMQ::password, topics, 2);
    mqttClient.loop();
    delay(10);
}
