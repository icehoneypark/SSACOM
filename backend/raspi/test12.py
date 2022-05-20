
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation
from collections import deque

import time
import threading

# -------------------초기세팅-----------------------------

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# packet = bytearray()
# packet.append(0x53)  # STX1:S
# packet.append(0xf1)  # STX2
# packet.append(0x09)  # len
# packet.append(0x00)  # len
# packet.append(0x06)  # data
# packet.append(0x53)  # S
# packet.append(0x45)  # E
# packet.append(0x4e)  # N
# packet.append(0x44)  # D
# packet.append(0x5f)  # _
# packet.append(0x5f)  # _
# packet.append(0x4f)  # O
# packet.append(0x4e)  # N
# packet.append(0x8B)  # CHECKSUM
# packet.append(0x45)  # ETX:E

ser = serial.Serial(
    port='COM5',
    #baudrate = 9600,
    baudrate=115200,
    # baudrate=921600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=10
)

fig = plt.figure()
dimension = (80, 40)
# data = np.zeros(dimension[0], dimension[1])
sns.heatmap(np.zeros(dimension), vmax=5000, vmin=600)

# ser = serial.Serial(
#     port='COM5',
#     #baudrate = 9600,
#     baudrate=115200,
#     # baudrate = 921600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
# )

data_r = deque()
for i in range(80):
    data_r.append([0] * 40)


def read_module():
    data = []
    data_cnt = 0
    while 1:
        tmp1 = ser.read().hex()
        tmp2 = ser.read().hex()
        tmp_int = int(tmp2 + tmp1, 16)

        data.append(tmp_int)
        data_cnt += 1
        if data_cnt == 40:
            data_r.popleft()
            data_r.append(data)
            data_cnt = 0
            data = []


read_data_thread = threading.Thread(target=read_module)
read_data_thread.start()


def init():
    sns.heatmap(np.zeros(dimension), vmin=600, vmax=5000, cbar=False)


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
        sns.heatmap(data_r, vmax=5000, vmin=600, cbar=True)
        reset_cnt = 0
    else:
        sns.heatmap(data_r, vmax=5000, vmin=600, cbar=False)

    reset_cnt += 1
    print(time.time() - start)


anim = animation.FuncAnimation(
    fig, animate, init_func=init, interval=10, repeat=False)

plt.show()