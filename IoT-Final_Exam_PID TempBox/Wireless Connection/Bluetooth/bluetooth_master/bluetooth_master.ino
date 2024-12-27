#include <BluetoothSerial.h>

// Create a BluetoothSerial object for Bluetooth communication
BluetoothSerial SerialBT;

// Counter for sent messages
int counter = 1;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_Master", true); // Enable Master mode
  Serial.println("ESP32 Master Bluetooth Serial Started. Discoverable as ESP32_Master.");

  // Try to connect to the slave
  while (!SerialBT.connect("ESP32_Slave")) {
    Serial.println("Trying to connect to ESP32_Slave...");
    delay(1000);
  }
  Serial.println("Connected to ESP32_Slave");
}

void loop() {
  // Create a message with the counter value
  String message = "Hello from Master! Count: " + String(counter++);
  SerialBT.println(message); // Send the message to the slave
  Serial.println("Sent to Slave: " + message);

  // Check for a response from the slave
  if (SerialBT.available()) {
    String response = SerialBT.readStringUntil('\n');
    Serial.println("Received from Slave: " + response);
  }

  delay(2000); // Send every 2 seconds
}
