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

def parsing_data(data,cnt):

    len_data = len(data)
    print(cnt)
    time.sleep(0.1)
    f = open("/home/pi/data.txt","a")
    for i in range(0,len_data):
        f.write(data[i])
        f.write(" ")        
    f.write("\n")
    f.close()
    

def readThread(ser):
    global line
    global exitThread
    global packet
    import time
    ser.read_all()
    ser.write(packet)
    
    time.sleep(2)
    cnt=0
    while not exitThread:
        
        STX1 = ser.read(1).hex()
        
        if(STX1=='53'):
            
            line.append(STX1)
            STX2 = ser.read(1).hex()
            if(STX2=='f1'):
                
                line.append(STX2)
            elif(STX2=='f2'):
                
                line.append(STX2)
            elif(STX2 =='f3'):
                
                line.append(STX2)
            else:
                line =[]
                continue
            
            len = ser.read(1).hex()
            line.append(len)
            len = ser.read(1).hex()
            line.append(len)
            for i in range(0,959):
                data = ser.read(1).hex()
                line.append(data)
            cnt+=1
            parsing_data(line,cnt)
            line = []
                            
                


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
time.sleep(2)
thread.start()
f.close()

