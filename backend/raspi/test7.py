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
    
    print("------------")
    print(cnt)
    len_data = len(data)
    print(len(data))
    prev_idx = 0
    idx = 10
    K = int(len_data/10)
    for i in range(0,K) :
        print(data[prev_idx:idx])
        prev_idx +=10
        idx +=10
    print(data[prev_idx:])
    print("---------------")
    

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
            
            len1 = ser.read(1).hex()
            line.append(len1)
            len2 =  ser.read(1).hex()
            line.append(len2)
            
            time = 0
            while(1):
                time += 1
                
                if(time >=100000):
                    print("time error")
                    
                    line=[]
                    break
                
                data = ser.read(1).hex()
                if(data=='53'):
                    
                    line.append(data)
                    tmp = ser.read(1).hex()
                    if(tmp=='45'):
                        line.append(tmp)
                        tmp = ser.read(1).hex()
                        if(tmp=='4e'):
                            line.append(tmp)
                            tmp = ser.read(1).hex()
                            if(tmp=='44'):
                                line.append(tmp)
                                tmp = ser.read(1).hex() # _
                                line.append(tmp)
                                tmp = ser.read(1).hex() #_
                                line.append(tmp)
                                tmp = ser.read(1).hex() # O
                                line.append(tmp)
                                tmp = ser.read(1).hex() # N
                                line.append(tmp)
                                tmp = ser.read(1).hex() # checksum
                                line.append(tmp)
                                tmp = ser.read(1).hex() # E
                                line.append(tmp)
                                cnt+=1
                                parsing_data(line,cnt)
                                line = []
                            else:
                                line.append(tmp)
                                
                        else:
                            line.append(tmp)
                            

                        break
                    else :
                        line.append(tmp)
                        
                    
                        
                else:
                    line.append(data)
            
      
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

