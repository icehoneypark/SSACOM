
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
from collections import deque
import serial
import time
import threading
from skimage import color 
from skimage import filters
from skimage import io 
from skimage.morphology import disk

# -------------------초기세팅-----------------------------

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
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
    baudrate=115200,
    # baudrate=921600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


fig = plt.figure()
data_width = 40
dimension = (80, data_width)
# data = np.zeros(dimension[0], dimension[1])
sns.heatmap(np.zeros(dimension), vmax=5000, vmin=600)

# fig2 = plt.figure()
# sns.heatmap(np.zeros(dimension), vmax=5000, vmin = 600)

data_r = deque()
data_pool = deque()
for i in range(80):
    data_pool.append([0] * data_width)


def read_module():
    ser.read_all()
    ser.write(packet)
    
    buffer_cnt = 0
    while 1:
        if(ser.read() == b'S'):
            if(ser.read() == b'\xf2'):
                if(ser.read(13).hex() == '09000653454e44000000f93245'):
                    break
                else:
                    print('통신실패')

    data = []
    data_cnt = 0
    while 1:
        frame_cnt = 0
        while 1:
            if ser.read(1).hex() == '53':
                if ser.read(1).hex() == 'f3':
                    if ser.read(1).hex() == '06':
                        break
                    else:
                        print("탐색중3")
                else:
                    print("탐색중2")
            else:
                print("탐색중")
        while 1:
            tmp1 = ser.read(1).hex()
            tmp2 = ser.read(1).hex()
            tmp_int = int(tmp2 + tmp1, 16)
            data.append(tmp_int)
            data_cnt += 1
            if data_cnt == data_width:
                
                data_r.append(data)
                data_cnt = 0
                data = []
                frame_cnt += 1
                        
            if frame_cnt == 12:
                list = []
                for i in range(0,12):
                    list.append(data_r.popleft())       

                # np_list = np.array(list)
                # pool_data = min_pooling(np_list)
                # pool_data_list = pool_data.tolist()
                # print(pool_data_list)
                # pool_data = []
                # for i in range (0,40):
                #     minList = []
                #     for k in range(0,12):
                #         minList.append(list[k][i])
                        
                #     minVal = min(minList)
                #     pool_data.append(minVal)
                # for i in range(0,40):
                #     pool_data_normal.append( (pool_data[i] - minVal) / (maxVal - minVal) )

                # normalization
                for i in range(0,12):
                    minVal = min(list[i][:])
                    maxVal = max(list[i][:])
                    for j in range(0,40):
                        list[i][j] = (list[i][j] - minVal) / (maxVal - minVal)


                # 3 by 3 median filter
                filter_size = 3
                for r in range(0,12-filter_size+1):                    
                    
                    for c in range(0,40-filter_size+1):
                        tmp_list = []
                        for i in range(0,filter_size):
                            for j in range(0,filter_size):
                                tmp_list.append(list[r+i][c+j])

                        sorted_list = sorted(tmp_list)
                        list_val = sorted_list[int(filter_size*filter_size/2)]
                        list[r][c] = list_val



                # push data
                for i in range(0,12):

                    data_pool.popleft()
                    data_pool.append(list[i][:])
                
                frame_cnt = 0
                buffer_cnt += 1
                break

        ser.read(963)
        # ser.read(963)


read_data_thread = threading.Thread(target=read_module)
read_data_thread.start()


def init():
    sns.heatmap(np.zeros(dimension), vmin=0, vmax=1, cbar=False)


reset_cnt = 0

def min_pooling(arr):
    x, y = arr.shape

    pool_size= 12
    new_x, new_y = x//pool_size , y

    arr = np.min(arr.reshape(new_x, pool_size, y, 1), axis = (1,3))
    return arr

def animate(i):
    # print("길이", len(data_r))
    global reset_cnt
    start = time.time()
    # print(data_r)
    # 10번마다 리셋해서 속도를 유지
    if reset_cnt == 10:
        plt.clf()
        # 리셋하면 우측에 cbar가 날아가버리는 현상발생
    
        sns.heatmap(data_pool, vmin=0, vmax=1, cbar=True)
        reset_cnt = 0
    else:
        sns.heatmap(data_pool, vmin=0, vmax=1, cbar=False)

    reset_cnt += 1
    # print(time.time() - start)


anim = animation.FuncAnimation(
    fig, animate, init_func=init, interval=10, repeat=False)

plt.show()
