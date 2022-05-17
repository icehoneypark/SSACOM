import serial
import time
import signal
import threading

#라인 단위로 데이터 가져올 리스트 변수
line = list() 

# packet 정보
packet = bytearray()
packet.append(0x53)#STX1:S
packet.append(0xf1)#STX2
packet.append(0x09)#len
packet.append(0x00)#len
packet.append(0x06)#data
packet.append(0x53)#S
packet.append(0x45)#E
packet.append(0x4e)#N
packet.append(0x44)#D
packet.append(0x5f)#_
packet.append(0x5f)#_
packet.append(0x4f)#O
packet.append(0x4e)#N
packet.append(0x8B)#CHECKSUM
packet.append(0x45)#ETX:E

# 쓰레드 종료용 변수
exitThread = False

#쓰레드 종료용 시그널 함수
def handler(signum, frame):
     exitThread = True


#데이터 처리할 함수
def parsing_data(data):
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침

    #출력!
    print("*******************")
    print(data)

#본 쓰레드
def readThread(ser):
    global line
    global exitThread
    global packet

    ser.write(packet)

    # 쓰레드 종료될때까지 계속 돌림
    while not exitThread:
        #데이터가 있있다면
        for c in ser.read():
            #line 변수에 차곡차곡 추가하여 넣는다.
            line.append(c)

            if c == 40: #라인의 끝을 만나면..
                #데이터 처리 함수로 호출
                parsing_data(line)

                #line 변수 초기화
                del line[:]                

if __name__ == "__main__":
    #종료 시그널 등록
    signal.signal(signal.SIGINT, handler)

    #시리얼 열기
    # ser = serial.Serial(port, baud, timeout=0)
    ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    )
    # ser.ser_buffer_size(rx_size=115200, tx_size=115200)

    #시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=readThread, args=(ser,))

    #시작!
    thread.start()