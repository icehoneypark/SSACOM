### 라즈베리파이 웹소켓 통신

```python
import asyncio
import websockets

async def connect():
	async with websockets.connect("ws://k6s105.p.ssafy.io:30002") as websocket:
		for i in range(1, 10, 1):
			await websocket.send("hello socket!!");
			data = await websocket.recv();
			print(data);
			
asyncio.get_event_loop().run_until_complete(connect())
```

##### 라즈베리파이와 nodejs 웹소켓 통신 화면 (좌측 : 라즈베리파이(client), 우측 : nodejs(server))

![image-20220504182730708](raspberrypi.assets/image-20220504182730708.png)

### 스위치 동작에 따른 WebSocket 통신

```python
import asyncio
import websockets
import RPi.GPIO as GPIO
import time

sw=4
led=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(led,GPIO.OUT)

async def connect():
    async with websockets.connect("ws://k6s105.p.ssafy.io:30002") as websocket:
        try:
            while 1:
                if GPIO.input(sw)==1:
                    GPIO.output(led,GPIO.HIGH)
                    await websocket.send("LED ON!!");
                    print("LED ON!!");
                else :
                    GPIO.output(led,GPIO.LOW)
                    await websocket.send("LED OFF!!");
                    print("LED OFF!!");
                time.sleep(1)
        except KeyboardInterrupt:
            GPIO.cleanup()

asyncio.get_event_loop().run_until_complete(connect())
```

![ezgif.com-gif-maker (1)](raspberrypi.assets/ezgif.com-gif-maker (1).gif)

### API GET, POST 요청 (동작 확인 완료)

```python
import requests
import json 

# GET 
# res = requests.get('http://k6s105.p.ssafy.io:8000/qna/') 
# print(str(res.status_code) + " | " + res.text) 

# POST (JSON) 
headers = {'Content-Type': 'application/json; chearset=utf-8'}
data = {
    "title": "test_title",
    "content": "test_content",
    "category": "test_category"
}
res = requests.post('http://k6s105.p.ssafy.io:8000/qna/', data=json.dumps(data), headers=headers) 
print(str(res.status_code) + " | " + res.text)
```



# 모듈 Serial 통신 데이터

### UART to USB 모듈 사용 (컴퓨터 연결)

![image-20220506172251743](raspberrypi.assets/image-20220506172251743.png)

![image-20220506172136341](raspberrypi.assets/image-20220506172136341.png)

![image-20220506172319061](raspberrypi.assets/image-20220506172319061.png)

### 라즈베리파이와의 연결

```python
# sudo pip install pyserial
# pyserial 설치 이후 실행 가능
# sudo python3 brstest.py (serial 통신이라 sudo 권한 필요)
# tx는 14, rx는 15번 gpio 사용

import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 115200)

a = 0

while True:
	print("started => {} ".format(a))
	received_data =ser.read()
	sleep(0.03)
	data_left = ser.inWaiting()
	received_data += ser.read(data_left)
	print (received_data)
	ser.write(received_data)
	a += 1
```

![image-20220506165114469](raspberrypi.assets/image-20220506165114469.png)![image-20220506172429029](raspberrypi.assets/image-20220506172429029.png)