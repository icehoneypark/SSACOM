import serial

import time

import signal

import threading

 

line = list()

 

#packet

 

packet = bytearray()

packet.append(0x53) # STX1 : S

packet.append(0xf1) # STX2

packet.append(0x09) # len

packet.append(0x00) # len

packet.append(0x06) # data

packet.append(0x53) # S

packet.append(0x45) # E

packet.append(0x4e) # N

packet.append(0x44) # D

packet.append(0x5f) # _

packet.append(0x5f) # _

packet.append(0x4f) # O

packet.append(0x4e) # N

packet.append(0x8B) #CheckSum

packet.append(0x45) #ETX:E

 

exitThread = False

 

 

def handler(signum, frame):

    exitThread = True

 

def parsing_data(data):

    print("------------")

    print(data)

 

 

def readThread(ser):

    global line

    global exitThread

    global packet

 

    ser.write(packet)

 

    while not exitThread:

        dataSize = 2;

        for i in range(40*dataSize):

                    

            tmp = ser.read(dataSize).hex()

            #print("wwwwwwwwwwwwwwwwwwwww")

            #print(tmp)

            if(len(tmp) >=2):

                realVal = int(tmp[dataSize:] + tmp[:dataSize], 16)

                

            #print(realVal)

                        

            line.append(realVal)

 

        parsing_data(line)

 

        del line[:]

        frameCnt = 120

    

        frameCnt -=1;

        

        if(frameCnt==0):

            framCnt = 120

            tmp = ser.read(9600).hex()

 

 

signal.signal(signal.SIGINT, handler)

 

ser = serial.Serial(

    port='/dev/ttyAMA0',

    baudrate = 115200,

    parity = serial.PARITY_NONE,

    stopbits = serial.STOPBITS_ONE,

    bytesize = serial.EIGHTBITS,

    timeout= 0

)

 

thread = threading.Thread(target=readThread, args=(ser,))

 

thread.start()