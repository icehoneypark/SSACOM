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