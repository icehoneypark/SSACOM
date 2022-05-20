먼저  pyserial을 설치해야된다

```
pip install pyserial
```

그리고 아두이노 본체쪽 유선연결 후 아두이노 코딩

파이썬 시리얼 코딩을 해야됨

예제

아두이노 코딩

```
int val;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(val++);
}
```

파이썬 코딩

```
import serial

ser = serial.Serial(
    port='com3', 
    baudrate=9600,
)

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-1])
```

나는 포트번호가 com3이고 보드레이트가 9600으로 하였음.



led 점등 a b c 

아두이노 코딩

```
#define OFFMODE -1
#define ONMODE 0
#define BLINKMODE 1
const int pinLED = 8;

char ch;
int state = OFFMODE;

void setup() {
  pinMode(pinLED,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    ch = Serial.read();
  }
  if(ch=='a'){
    state=ONMODE;
  }else if(ch=='b'){
    state=BLINKMODE;
  }else{
    state=OFFMODE;
  }
  
  if(state==ONMODE){
    digitalWrite(pinLED,HIGH);
  }else if(state==BLINKMODE){
    digitalWrite(pinLED,HIGH);
    delay(100);
    digitalWrite(pinLED,LOW);
    delay(100);
  }
  else{
    digitalWrite(pinLED,LOW);
  }
}
```

파이썬 코딩

```
import serial

ser = serial.Serial(
    port='com3',
    baudrate=9600,	
)

while True:
    print("insert op :", end=' ')
    op = input()
    ser.write(op.encode())
```

온습도 아누이도

```
#include <DHT11.h>

DHT11 dht11(7); 

void setup() {
  Serial.begin(9600);
}

void loop() {
  float humi, temp;
  int result = dht11.read(humi, temp);
  
    if(result == 0){
    Serial.print("humidity:");
    Serial.println(humi);
    Serial.print("temperature:");
    Serial.println(temp);
  }
  else {
    Serial.print("Error:");
    Serial.print(result);
  }
  delay(1000);
}
```

파이썬

```python
from datetime import datetime
import json

import serial
import requests

URL = 'http://127.0.0.1:8000/'


ser = serial.Serial(
    port='com3',  
    baudrate=9600,
)

print('아두이노와 통신 시작')

while True:

    try:
        if ser.readable():
            res = ser.readline()
            json_data = json.loads(res.decode()[:-1])
            json_data['time'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            print(json_data)
            client = requests.session()

            client.get(URL)  # sets cookie

            if 'csrftoken' in client.cookies:
                csrf_token = client.cookies['csrftoken']
            else:
                csrf_token = client.cookies['csrf']

            sensor_data = dict(
                **json_data,
                csrfmiddlewaretoken=csrf_token
            )
            response = client.post(URL, data=sensor_data, headers=dict(Referer=URL))
            print(f'아두이노 데이터 {URL} 전송: {response}\n')

    except serial.serialutil.SerialException:
        print('아두이노가 연결되어 있지 않습니다.\n')
        break

    except requests.exceptions.ConnectionError:
        print('인터넷 전송이 불가능합니다.\n')
        continue

    except KeyboardInterrupt:
        print('아두이노 시리얼 통신을 중단합니다.\n')
        break
```

