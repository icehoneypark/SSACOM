#include <SoftwareSerial.h>

SoftwareSerial s(0, 1);

char data;

int idx = 0;

int line = 0;

int block = 0;

unsigned char packet[] = {0x53, 0xf1, 0x09, 0x00, 0x06, 0x53, 0x45, 0x4e, 0x44, 0x5f, 0x5f, 0x4f, 0x4e, 0x8B, 0x45};


void setup() {
  Serial.begin(115200);
  s.begin(115200);
  Serial.println("Start Receive");
  Serial.println(block);
}

void loop() {
  
  char temp[40] = {0};
  
  s.write(packet, 15);
  
  //s.write((uint8_t*)packet, sizeof(packet));
  
  if(s.available()){

    byte data = s.readBytes(temp, 40);

    Serial.print("Input data Lenght : ");
    Serial.println(data);  
    for(int i = 0; i < data; i++) Serial.print(temp[i]);  
    Serial.println();
    
    // unsigned char data = s.read();
    Serial.print(data);
    Serial.print(' ');
    idx++;

    if(idx == 10){
      line++;
      Serial.println(' ');
      idx = 0;
      if(line == 4){
        block++;
        Serial.println(' ');
        Serial.print("block ");
        Serial.println(block);
        line = 0;
      }
    }
  }
}
