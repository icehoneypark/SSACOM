import serial
import time
import signal
import threading
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

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

ser.write(packet)

print(ser.read(15).hex())


start = time.time()

ser.read(14400).hex()

print(time.time() - start)