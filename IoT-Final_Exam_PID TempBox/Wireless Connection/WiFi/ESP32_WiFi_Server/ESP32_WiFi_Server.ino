#include "WiFi.h"
#include "ESPAsyncWebServer.h"

// Đặt thông tin mạng Wi-Fi
const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";

// Tạo đối tượng server sử dụng AsyncWebServer
AsyncWebServer server(80);

// Biến count để đếm số lần yêu cầu
int count = 0;

void setup() {
  // Khởi tạo Serial để debug
  Serial.begin(115200);
  Serial.println();
  
  // Đặt ESP32 làm Access Point
  Serial.print("Setting AP (Access Point)…");
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  // Đặt endpoint trả về "Hello from server" kèm theo giá trị của count
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    count++;  // Tăng biến count mỗi lần có yêu cầu
    String response = "Hello from server. Request count: " + String(count);
    
    // In thông tin ra Serial Monitor
    Serial.println("Received request, count: " + String(count));
    Serial.println("Responding with: " + response);
    
    request->send(200, "text/plain", response);
  });
  
  // Khởi động server
  server.begin();
}

void loop() {
  // Không cần thực hiện gì trong loop() vì server xử lý hết
}
