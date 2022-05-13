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

exitThread = False

#데이터 처리할 함수
def parsing_data(datas):
    global line, count
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침

    

    #출력!
    print("******** {} ***********".format(count))
    count += 1

    """
    for idx in range(20):
        data = datas[idx * 4 + 2] + datas[idx * 4 + 3]
        line.append(data)
        data = datas[idx * 4] + datas[idx * 4 + 1]
        line.append(data)
    """

    #print(line[:10])
    #print(line[10:20])
    #print(line[20:30])
    #print(line[30:40])


    """
    # normalize
    x = list()
    for _ in range(4):
        for idx in range(10):
            x.append(idx)

    x_array = np.array(x)

    y_array = np.array(line)

    normalized_arr = preprocessing.normalize([y_array])
    plt.scatter(x_array, y_array)
    plt.show()
    """

#본 쓰레드
def readThread(ser):
    global line, tmp
    global exitThread
    global packet, status
    global count

    #ser.flush()
    #ser.flushInput()
    #ser.flushOutput()
    # ser.read_all()
    # ser.write(packet)
            
    data_80 = deque()
    real_data = list()
    real_real_data = list()
    ser.write(packet)
    tmp_data = ser.read(15).hex()
    print(tmp_data)
    before = "45"

    real_real_data = list()

    while 1:

        #tmp_data = ser.read().hex()
        
        # print("count = {}".format(count))

        # print(tmp_data, end=" ")
        count += 1
        tmp_data = ser.read(963).hex()

        # real_data = list(tmp_data[4:1924])
    
        real_data = list(tmp_data[6:])
        
        for idx in range(960):
            data1 = real_data[idx] + real_data[idx + 1]
            data2 = real_data[idx + 2] + real_data[idx + 3]

            data = data2 + data1
            #real_real_data.append(data)
            real_real_data.append(int(data, 16))


        print("========= {} =========".format(count))

        for idx in range(int(len(real_real_data) / 10)):
            print(real_real_data[idx * 10 : idx * 10 + 10])

        real_real_data = list()

        # ser.read_all()
        # print(data_960)
        if len(data_80) > 80:
            
            pass
        """

        """
        if len(tmp_data) > 1:
            pass

        # count += 1
        if count == 10:
            break
        
        #parsing_data(tmp)

        # line 변수 초기화
        #del line[:]
        #del tmp[:] 
        

ser = serial.Serial(
	port='COM6',
	baudrate = 115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

readThread(ser)