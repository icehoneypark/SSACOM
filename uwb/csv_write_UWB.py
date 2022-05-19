import csv
import serial
import time
import signal
import threading
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

print("go!")
time.sleep(60)
print("waked up")

def min_pooling(arr):
    x, y = arr.shape
    # new_x, new_y = x//2 , y//2
    new_x, new_y = x//10 , y//10

    # arr = np.min(arr.reshape(new_x, 2, y, 1), axis = (1,3))
    arr = np.min(arr.reshape(new_x, 10, y, 1), axis = (1,3))
    return arr

## csv 파일에 들어갈 데이터
data = list()

## 파일명 설정
f = open("data.csv", "w", newline="")
writer = csv.writer(f)


## 패킷 전송 함수
def ser_start():
	ser.write(packet)

	while 1:
		if(ser.read() == b'S'):
			if(ser.read() == b'\xf2'):
				print(ser.read(13).hex())
				break

count = 0
## packet 정보
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

## serial 통신 설정 정보
ser = serial.Serial(
	port='COM6',
    #baudrate = 9600,
	baudrate = 115200,
	#baudrate = 921600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

## serial packet 전송
ser_start()

## 시간 측정
start = time.time()

#print(ser.read(15).hex())

y = 0

# for _ in range(12):
for act in range(1, 101):
	#print(ser.read(3).hex())
	while 1:
		if(ser.read().hex() == "53"):
			if(ser.read().hex() == "f3"):
				# if(ser.read().hex() == "06"):
					# break
				# ser.read().hex()
				print("act = {}, {}".format(act, ser.read().hex()))
				break

	data_tmp = list()
	count = 0

	while 1 :
		tmp1 = ser.read().hex()
		
		tmp2 = ser.read().hex()

		tmp = tmp2 + tmp1

		tmp_int = int(tmp, 16)

		data_tmp.append(tmp_int)

		if len(data_tmp) == 40:
			data.append(data_tmp)
			data_tmp = list()
			count += 1
			y += 1

		if count == 12:
			ser.read(963)
			ser.read(963)
			#ser.read_all()
			break
	# if act % 100 == 0:
	# 	trash = ser.read_all()
	# 	ser_start()


## 데이터 작성
# data = np.array(data)
# data = min_pooling(data)
writer.writerows(data)
f.close()

print(time.time() - start)

# 표 그리기
#plt.show()