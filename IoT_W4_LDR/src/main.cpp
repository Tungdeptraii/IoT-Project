#include <Arduino.h>


void setup() {
  Serial.begin(115200);
}

void loop() {
  int analogValue = analogRead(LDR_PIN);
  Serial.print(">analogValue:");
  Serial.println(analogValue);
  delay(10);
}

