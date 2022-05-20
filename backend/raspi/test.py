
import serial
from time import sleep

ser = serial.Serial("/dev/ttyAMA0",115200)

a=0

data_list = list()

while True:
    print("started=>{}".format(a))
    received_data = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()
    received_data += ser.read(data_left)
    data_list.append(received_data)
    print(data_list)
    data_list = list()
    a +=1

