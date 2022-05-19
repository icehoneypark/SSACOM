# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .serializers import tempSerializer
pre_temp = 0
pre_humi = 0
class DataConsumer(WebsocketConsumer):
    
    # 1. self.scope['url_route']['kwargs']['room_name']
    #   - self.scope : 각 Consumer 에서 연결정보를 가지고 있는 변수
    #   - 위 코드 처럼 작성하는 경우, room_name(group name)을 얻어올 수 있다.
    #   - 또한, 소켓 통신을 연결한 사용자가 인증된 사용자인지도 검증 가능하다.
    # 2. self.room_group_name = 'chat_%s' % self.room_name
    #   - 해당 채널이 속하는 그룹의 이름을 정해주는 부분.
    #   - 위와 같이 작성하여 해당 채널이 속하는 그룹의 이름을 정할 수 있다.
    #   - 그룹이름은 숫자, 알파벳, "_", 마침표 만 들어갈 수 있다.
    # 3. async_to_sync(self.channel_layer.group_add)(...)
    #   - self.channel_layer.group_add = 실제로 채널을 그룹에 등록하는 함수
    #   - 해당 함수는 기본적으로 비동기로 작동하기 때문에 async_to_sync 함수를 통해 동기모드로 실행을 하였다.
    #   - self.room_group_name 으로 이름을 정했다고 하더라도, 이미 있는 이름인 경우 실패할 수 있다.
    # 4. self.accept()
    #   - 연결을 요청한 사용자와 연결을 허용해 주는 함수
    #   - 소켓의 accept 함수와 같은 역할을 수행함
    # 5. async_to_sync(self.channel_layer.group_discard)(...)
    #   - 그룹에서 등록을 해제하는 함수
    # 6. async_to_sync(self.channel_layer.group_send)
    #   - 실제로 그룹에 속한 모든 채널에 메시지를 보내는 함수
    #   - 'type'을 이용해서 실제 메시지를 수신했을때의 이벤트 핸들러를 지정해 줄 수 있다.
    #   - 이번 예제에서는 chat_message 함수를 핸들러 함수로 지정하였다.

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        # data를 json형태로 받아서 메시지 부분을 파싱
        global pre_temp , pre_humi
        text_data_json = json.loads(text_data)
        humi = text_data_json['humi']
        temp = text_data_json['temp']
        
        print('받은 데이터 :', humi, temp)
      
        serializer = tempSerializer(data = text_data_json)

        
        if serializer.is_valid(raise_exception=True) and pre_temp != temp and pre_humi != humi :
            pre_temp = temp
            pre_humi = humi
            serializer.save()
        # 데이터 수신만 하면되기 때문에 일단 주석처리
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )
        
        

    # Receive message from room group
    def chat_message(self, event):
        print('여기는 chat_message')
        message = event['message']
        print('r data :', message)
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))