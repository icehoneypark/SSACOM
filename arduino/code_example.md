# 코드 예제
## 아두이노에 작성할 C++ 코드 예제를 마크다운 형식으로 만들어 작성

String ssid		= "wifi id"; // 와이파이 아이디 기입
String password	= "password"; // 와이파이 패스워드 기입
String host		= "api.thingspeack.com"; // api요청 host
const int httpPort	= 80;
String uri		= "update?api_key=CZFC7FBN2ZEFSCVB&field1="; // api 요청 uri
  
int setupESP8266(void){
  	// ESP8266 시리얼 통신 시작
  	Serial.begin(115200);
  	
	// 모듈 연결 확인
  	Serial.println("AT");
  	// 사용가능 와이파이 불러오기
	Serial.println("AT+CWLAP");
  	delay(1000);
  	if(!Serial.find("OK")) return 1;
  
  	// 회로와 시뮬레이터 와이파이 연결
  	Serial.println("AT+CWJAP=\"" + ssid + "\",\"" + password + "\"");
	delay(1000);
  	if(!Serial.find("OK")) return 2;
  
  	// host와 TCP 연결 열기
  	Serial.println("AT+CIPSTART=\"TCP\",\"" + host + "\", " + httpPort);
   	delay(5000);
 	if(!Serial.find("OK")) return 3;
  
  	return 0;
}

void anydata(void) {
	int temp = map(analogRead(A0),20,358,-40,125);
  
  	// http call
	String httpPacket = "GET" + uri + String(temp) + " HTTP/1.1\r\nHost: " + host + "\r\n\r\n";
	int length = httpPacket.length();
  
  	// send our message length
  	Serial.print("AT+CIPSEND=");
  	Serial.println(length);
  	delay(10);
  
  	// send our http request
  	Serial.print(httpPacket);
  	delay(10);
  	if(!Serial.find("SEND OK\r\n")) return;
  
}

void setup() {
  	
  	setupESP8266();
}

void loop() {
  	// 센서값 읽어서 api요청
  	anydata();
  	// 10초 딜레이후 루프 실행
  	delay(10000);
}