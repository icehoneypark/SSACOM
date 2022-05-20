from collections import deque
import serial
import time

# import signal

# import threading

# from sklearn import preprocessing

# from collections import deque

 

# List variable to get data line by line

 

count = 0

# packet information

packet = bytearray()

packet.append(0x53) # STX1:S

packet. append(0xf1) # STX2

packet. append(0x09) # len

packet. append(0x00) # len

packet. append(0x06) # data

packet. append(0x53) # S

packet. append(0x45) # E

packet.append(0x4e) # N

packet. append(0x44) # D

packet. append(0x5f) # _

packet. append(0x5f) # _

packet. append(0x4f) # O

packet.append(0x4e) # N

packet. append(0x8B) # CHECKSUM

packet.append(0x45) # ETX:E

 
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout= 0
)
 

ser.write(packet)

temp = time.time()

while 1:

    if(ser.read() == b'S'):

        if(ser.read() == b'\xf2'):

            print(ser.read(13).hex())

            break

print('Time to empty the buffer and find a new one:', time.time()-temp)

 

 

result = []

start = time.time()

 

res = deque()

for _ in range(2):

    res. append([0 for _ in range(40)])

 

for _ in range(60):

    print(ser.read(3).hex())

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

            res. append(data)

            # res.popleft()

            data = list()

            count += 1

            cnt = 0

