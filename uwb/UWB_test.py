import serial
import time
import signal
import threading
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def ser_start():
	ser.write(packet)

	while 1:
		if(ser.read() == b'S'):
			if(ser.read() == b'\xf2'):
				print(ser.read(13).hex())
				break

#라인 단위로 데이터 가져올 리스트 변수
line = list()
tmp = list()

count = 0
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

ser = serial.Serial(
	port='COM6',
    #baudrate = 9600,
	baudrate = 115200,
	#baudrate = 921600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

# 표 외부 설정
plt.title("data viewer")
plt.ylabel("count")
plt.xlabel("length")

"""
ser.write(packet)

while 1:
    if(ser.read() == b'S'):
        if(ser.read() == b'\xf2'):
            print(ser.read(13).hex())
            break
"""

ser_start()

start = time.time()

#print(ser.read(15).hex())

#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = 0

#cnt = 15

#for _ in range(240):
for act in range(1, 10000):
	#print(ser.read(3).hex())
	while 1:
		if(ser.read().hex() == "53"):
			if(ser.read().hex() == "f3"):
				#ser.read().hex()
				print(ser.read().hex(), end=" ")
                print("act = {}".format(act))
				break
	#cnt += 3

	data = list()
	count = 0

	#if cnt >= 14400:
	#	break

	while 1 :
		tmp1 = ser.read().hex()
		
		tmp2 = ser.read().hex()

		#cnt += 2

		#if cnt >= 14400:
		#	break

		tmp = tmp2 + tmp1

		tmp_int = int(tmp, 16)

		data.append(tmp_int)

			data = list()
			count += 1
			y += 1

		if count == 12:
			#ser.read_all()
            ser.read(963)
            ser.read(963)
			break
	if act % 80 == 0:
		#trash = ser.read_all()
		# ser_start()
		
print(time.time() - start)

# 표 그리기
plt.show()