import numpy as np
import serial
import time
from tensorflow.python.keras.models import load_model

# 라인 단위로 데이터 가져올 리스트 변수
model = load_model('test.h5')
count = 0

def min_pooling(arr):
    x, y = arr.shape
    new_x, new_y = x//2 , y//2

    arr = np.min(arr.reshape(new_x, 2, y, 1), axis = (1,3))
    return arr

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

start = time.time()

dum_list = list()
check_list = list()
tmp = list()

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
    count = 0
    cnt = 0
    while 1:
        tmp1 = ser.read().hex()
        tmp2 = ser.read().hex()
        tmp_int = int(tmp2 + tmp1, 16)

        cnt += 1
        tmp.append(tmp_int)
        if cnt == 40:
            count += 1
            cnt = 0
            check_list.append(tmp)
            tmp = list()

        if count == 12:
            count = 0
            ser.read(963)
            ser.read(963)
        #     trash = ser.read_all()
            if len(dum_list) == 0:
                dum_list.append(list(min_pooling(np.array(check_list).astype(np.int64))))
                check_list = list()
            # else:
            elif len(dum_list) == 1:
                dum_list[0].extend(list(min_pooling(np.array(check_list).astype(np.int64))))
                check_list = list()
                cnt_0 = 0
                cnt_1 = 0
                # predict = model.predict(dum_list)
                predict = model.predict(np.array(dum_list).astype(np.int64))
                for pre in predict:
                    if pre[1] < 0.5:
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
            break
    if act % 20 == 0:
        ser.read_all()
        # ser_start()
        

print(time.time() - start)
# plt.colorbar()
# plt.show()