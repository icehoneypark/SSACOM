Record Speaker 모듈

참고 사이트 : https://blog.naver.com/PostView.naver?blogId=eduino&logNo=221091706403&categoryNo=23&parentCategoryNo=0

```c++
int rec = 5;                                    // rec를 5번 핀으로 
int playe = 4;                                  // playe를 4번 핀으로
int command;                                    // 시리얼 모니터의 명령을 받아들이는 변수

void setup() 
{
  Serial.begin(9600);                          // 시리얼 통신, 속도는 9600
  pinMode (rec, INPUT);                         // rec를 입력으로
  pinMode (playe,OUTPUT);                       // playe를 출력으로
  Serial.println("*********command*********");  // 1. 녹음 10초 2. 재생
  Serial.println("1. record 10sec");
  Serial.println("2. play ");
}
 
void loop() {
  while(Serial.available()) 
  {                  // 시리얼 통신이 연결되어 있을시    
    
    command = Serial.read();                   // 시리얼 통신으로 한 명령 읽기
    
    switch(command) 
    {                             
      case '1':                                 // 1 입력 시 녹음 시작
        Serial.println("Recording 10 sec.....");
        digitalWrite(rec,HIGH);                 // 녹음 중....
        delay(10000);                           // 10초 동안 녹음 중 
        digitalWrite(rec,LOW);                  // 녹음 종료 
        Serial.println("Recording finished");
        break;
                
      case '2':                                 // 2 입력 시 녹음된 소리 재생
        Serial.println("play the record!!");
        digitalWrite(playe,HIGH);               // 재생 중.
        delay(10);
        digitalWrite(playe,LOW);                // 녹음된 소리 재생이 끝나면 low로 
        break;
    }
  }
}
```



```c++
int REC = 5;

int PLAYE = 6;
int PLAYL = 7;
int FT = 8;

char input;

void setup() {
  Serial.begin(9600);
  pinMode(REC, OUTPUT);
  pinMode(PLAYE, OUTPUT);
  pinMode(PLAYL, OUTPUT);
  pinMode(FT, OUTPUT);
}

void loop() {
  if(Serial.available())
  {
    input = Serial.read();
    
    if(input == 'R')
    {
      digitalWrite(REC,HIGH);
      Serial.println("REC...");
    }
    else if(input == 'E')
    {
      digitalWrite(PLAYE,HIGH);
      Serial.println("PLAYE...");
      digitalWrite(PLAYE,LOW);
    }
    else if(input == 'L')
    {
      digitalWrite(PLAYL,HIGH);
      Serial.println("PLAYL...");
      delay(10000);
      digitalWrite(PLAYL,LOW);
    }
    else if(input == 'F')
    {
      digitalWrite(FT,HIGH);
      Serial.println("FT...");
    }
    else if(input == 'S')
    {
      digitalWrite(REC,LOW);
      digitalWrite(FT,LOW);
      Serial.println("STOP...");
    }
    else
    {
      Serial.println("wrong input value");
    }
  }
} 
```

