# 115200 모듈 시각화 py

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
from collections import deque
import serial
import time
import threading
from tensorflow.python.keras.models import load_model

# -------------------초기세팅-----------------------------
model = load_model('test.h5')
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

data_r = deque()
for i in range(80):
    data_r.append([0] * data_width)


def read_module():
    dum_cnt = 0
    dum_list = list()
    check_list = list()
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
            tmp1 = ser.read().hex()
            tmp2 = ser.read().hex()
            tmp_int = int(tmp2 + tmp1, 16)
            data.append(tmp_int)
            data_cnt += 1
            if data_cnt == data_width:
                data_r.popleft()
                data_r.append(data)
                data_cnt = 0
                data = []
                frame_cnt += 1
                check_list.append(data)
            if frame_cnt == 12:
                frame_cnt = 0
                buffer_cnt += 1
                dum_list.append(check_list)
                dum_cnt += 1
                if dum_cnt == 3:
                    cnt_0 = 0
                    cnt_1 = 0
                    print("데이터 길이 : {}".format(len(dum_list)))
                    predict = model.predict(np.array(dum_list).astype(np.int64))
                    for pre in predict:
                        if pre[0] < 0.5:
                            cnt_0 += 1
                        else:
                            cnt_1 += 1
                    if cnt_0 > cnt_1:
                        print("=                 =")
                        print("==                =")
                        print("=  ==             =")
                        print("=    ==           =")
                        print("=      ==         =")
                        print("=        ==       =")
                        print("=          ==     =")
                        print("=            ==   =")
                        print("=              == =")
                        print("=                ==")
                    else:
                        print("=          =")
                        print(" =        =")
                        print("   =     =")
                        print("    =   =")
                        print("     = =")
                        print("      =")
                        print("      =")
                        print("      =")
                        print("      =")
                        print("      =")
                dum_list = list()
                check_list = list()
                dum_cnt = 0
                break
        ser.read(963)
        ser.read(963)


read_data_thread = threading.Thread(target=read_module)
read_data_thread.start()


def init():
    sns.heatmap(np.zeros(dimension), vmin=0, vmax=2700, cbar=False)


reset_cnt = 0


def animate(i):
    # print("길이", len(data_r))
    global reset_cnt
    start = time.time()
    # print(data_r)
    # 10번마다 리셋해서 속도를 유지
    if reset_cnt == 10:
        plt.clf()
        # 리셋하면 우측에 cbar가 날아가버리는 현상발생
        sns.heatmap(data_r, vmin=0, vmax=2700, cbar=True)
        reset_cnt = 0
    else:
        sns.heatmap(data_r, vmin=0, vmax=2700, cbar=False)

    reset_cnt += 1
    # print(time.time() - start)


anim = animation.FuncAnimation(
    fig, animate, init_func=init, interval=10, repeat=False)

plt.show()
