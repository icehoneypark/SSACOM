import serial
import time
import signal
import threading
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

#라인 단위로 데이터 가져올 리스트 변수
line = list()
tmp = list()

count = 1
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
    for idx in range(40):
        data1 = datas[idx * 4 + 2] + datas[idx * 4 + 3]
        data2 = datas[idx * 4] + datas[idx * 4 + 1]
        data = data1 + data2
        data = int(data, 16)
        line.append(data)
    """
    '''
    for idx in range(40):
        data = datas[idx * 2 + 1] + datas[idx * 2]
        data = int(data, 16)
        line.append(data)
    '''
    for idx in range(40):
        data = datas[idx * 2] + datas[idx * 2 + 1]
        #data = datas[idx * 2 + 1] + datas[idx * 2]
        data = int(data, 16)
        line.append(data)

    print(line[:10])
    print(line[10:20])
    print(line[20:30])
    print(line[30:40])
    

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
    ser.write(packet)
            
    while 1:
        #tmp_data = list(ser.read_all().hex())
        #ser.write(packet)
        tmp_data = ser.read_all()
        #tmp_data = ser.readline()
        #tmp_data = ser.read(200)
        print("횟수 : {}, 타입 : {}, 길이 : {}, 데이터 : {}".format(count, type(tmp_data), len(tmp_data), tmp_data))
        #if 0 < len(tmp_data) < 24:
        #    print("what? what? what? what? what? what? what? what?")
        # tmp_data = tmp_data.hex()
        if len(tmp_data) > 1:
            tmp_data_fir = list()
            tmp_data_fin = list()
            print("start")
        
            print("앞", "뒤")
            for idx in range(int(len(tmp_data) / 2)):
                print(tmp_data[idx * 2], tmp_data[idx * 2 + 1])
                tmp_data_fir.append(tmp_data[idx * 2] + tmp_data[idx * 2 + 1])
            print("end")
            """
            for idx in range(int(len(tmp_data_fir) / 2)):
                tmp_data_fin.append(int(tmp_data_fir[idx * 2 + 1] + tmp_data_fir[idx * 2], 16))
            print("read data = {}".format(tmp_data_fin))
            """
            '''
            for idx in range(int(len(tmp_data) / 4)):
                print(int(tmp_data[idx * 4 + 2] + tmp_data[idx * 4 + 3] + tmp_data[idx * 4] + tmp_data[idx * 4 + 1], 16), end=" ")
            print("")
            print("end")
            '''
        '''
        dd = list()
        ddd = list()
        if len(tmp_data) > 4:
            for idx in range(int(len(tmp_data)/ 2)):
                dd.append(tmp_data[idx * 2] + tmp_data[idx * 2 + 1])
            
            for idx in range(int(len(dd)/ 2)):
                ddd.append(int(dd[idx * 2 + 1] + tmp_data[idx * 2], 16))

            for k in range(len(ddd)):
                if ddd[k] > 10000:
                    print("fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck")
            
            print(ddd)
        
        '''
        #tmp.append(tmp_data)

        '''
        if len(tmp_data) >= 160:
            parsing_data(tmp_data)
            del line[:]
            del tmp[:]
        '''
        '''
        if len(tmp) == 80:
            parsing_data(tmp)
            del line[:]
            del tmp[:]
            #ser.flush()
            #ser.flushInput()
            #ser.flushOutput()
            ser.read_all()
        '''
        count += 1
        if count == 30:
            break
        
        """
        tmp = list(ser.read(80).hex())
        # tmp = list(ser.read(40).hex())

        # trash = ser.read(10000)
        """ 
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