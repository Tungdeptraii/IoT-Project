#include <BluetoothSerial.h>

// Create a BluetoothSerial object for Bluetooth communication
BluetoothSerial SerialBT;

// Counter for sent responses
int counter = 1;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_Slave"); // Slave mode
  Serial.println("ESP32 Slave Bluetooth Serial Started. Waiting for Master to connect...");

  // Wait for the master to connect
  while (!SerialBT.connected()) {
    delay(1000);
    Serial.println("Waiting for ESP32_Master to connect...");
  }
  Serial.println("Connected to ESP32_Master");
}

void loop() {
  // Check if a message is received from the master
  if (SerialBT.available()) {
    String message = SerialBT.readStringUntil('\n');
    Serial.println("Received from Master: " + message);

    // Create a response with the counter value
    String response = "Hello from Slave! Count: " + String(counter++);
    SerialBT.println(response); // Send the response to the master
    Serial.println("Sent to Master: " + response);
  }

  delay(50); // Small delay to avoid overwhelming the loop
}
