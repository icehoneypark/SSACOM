from collections import deque
import serial
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import signal
# import threading
# from sklearn import preprocessing
# from collections import deque

# 라인 단위로 데이터 가져올 리스트 변수
z
count = 0
# packet 정보
packet = bytearray()
packet.append(0x53)  # STX1:S
packet.append(0xf1)  # STX2
packet.append(0x09)  # len
packet.append(0x00)  # len
packet.append(0x06)  # data
packet.append(0x53)  # S
packet.append(0x45)  # E
packet.append(0x4e)  # N
packet.append(0x44)  # D
packet.append(0x5f)  # _
packet.append(0x5f)  # _
packet.append(0x4f)  # O
packet.append(0x4e)  # N
packet.append(0x8B)  # CHECKSUM
packet.append(0x45)  # ETX:E

ser = serial.Serial(
    port='COM6',
    #baudrate = 9600,
    baudrate=115200,
    # baudrate = 921600,,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

temp = time.time()

def ser_start():
    ser.write(packet)
    while 1:
        if(ser.read() == b'S'):
            if(ser.read() == b'\xf2'):
                print(ser.read(13).hex())
                break
    #print('버퍼 비우고 새로 찾는 시간 :', time.time()-temp)

ser_start()

result = []
start = time.time()

res = deque()
for _ in range(2):
    res.append([0 for _ in range(40)])

for act in range(1, 1001):
    print("act = {}".format(act))
# for _ in range(1000):
    while 1:
        if(ser.read().hex() == "53"):
            if(ser.read().hex() == "f3"):
                # print(ser.read().hex())
                if(ser.read().hex() == "06"):
                    break
    #print(ser.read(3).hex())
    data = list()
    count = 0
    cnt = 0
    while 1:
        tmp1 = ser.read().hex()
        tmp2 = ser.read().hex()
        tmp_int = int(tmp2 + tmp1, 16)

        data.append(tmp_int)
        cnt += 1
        if cnt == 40:
            # print(data)
            res.append(data)
            # res.popleft()
            data = list()
            count += 1
            cnt = 0

            #  그림 그리기
            # df = pd.DataFrame(res, columns=[x for x in range(40)])
            # df.index = [y for y in range(180)]

            plt.imshow(res, cmap='hot', interpolation='none')

            # plt.xticks(range(len(df.columns)), df.columns)
            # plt.yticks(range(len(df)), df.index)
            # plt.pause(0.05)

        if count == 12:
            ser.read(963)
            ser.read(963)
        #     trash = ser.read_all()
            break
    if act % 20 == 0:
        ser.read_all()
        # ser_start()
        

print(time.time() - start)
plt.colorbar()
plt.show()