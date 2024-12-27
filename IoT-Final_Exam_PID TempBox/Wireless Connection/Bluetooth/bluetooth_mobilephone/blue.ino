#include "BluetoothSerial.h"
#include "DHT.h"

// DHT11 Configuration
#define DHTPIN 13       // Pin connected to the DHT11 sensor
#define DHTTYPE DHT11  // Sensor type: DHT11

DHT dht(DHTPIN, DHTTYPE);
BluetoothSerial SerialBT;

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_DHT11"); // Bluetooth device name
  Serial.println("ESP32 is running. You can pair with Bluetooth!");
  
  dht.begin(); // Initialize the DHT11 sensor
}

void loop() {
  // Read data from the DHT11 sensor
  float temperature = dht.readTemperature(); // Read temperature
  float humidity = dht.readHumidity();       // Read humidity

  // Check for errors in reading data
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read data from DHT11!");
    SerialBT.println("Error: Failed to read data from the sensor!");
  } else {
    // Print data to the Serial Monitor
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.print("°C, Humidity: ");
    Serial.print(humidity);
    Serial.println("%");

    // Send data via Bluetooth
    String data = "Temperature: " + String(temperature) + "°C, Humidity: " + String(humidity) + "%";
    SerialBT.println(data);
  }

  delay(2000); // Wait 2 seconds before the next reading
}
