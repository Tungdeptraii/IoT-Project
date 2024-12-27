#include <WiFi.h>
#include <HTTPClient.h>

// Thông tin Wi-Fi kết nối với Access Point
const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";

// Địa chỉ của ESP32 Access Point
const char* serverName = "http://192.168.4.1/";

void setup() {
  Serial.begin(115200);
  
  // Kết nối vào Wi-Fi Access Point
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) { 
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Gửi HTTP GET request đến ESP32 để nhận thông điệp
  HTTPClient http;
  http.begin(serverName); // URL của server ESP32
  int httpResponseCode = http.GET();

  // In thông tin về phản hồi HTTP ra Serial
  if (httpResponseCode > 0) {
    String payload = http.getString();
    Serial.println("HTTP Response code: " + String(httpResponseCode));
    Serial.println("Received from server: " + payload);
  } else {
    Serial.print("Error on HTTP request: ");
    Serial.println(httpResponseCode);
  }
  
  http.end();
  
  delay(5000); // Gửi yêu cầu mỗi 5 giây
}
