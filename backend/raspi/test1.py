import time
import serial

def connect_serial(port):
    import serial
    ser = serial.Serial(
        port=port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits =serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0
    )

    ser.ser_buffer_size(rx_size=115200, tx_size=115200)
    packet = bytearray()
    packet.append(0x53) # STX1:s
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
    packet.append(0x8B) # CHECKSUM
    packet.append(0x45) # ETX:E

    ser.write(packet)

    return ser

connect_serial('/dev/ttyAMA1')


# parsing
while True :
    result = []
    for i in range(40*2):
        tmp = ser.read(2).hex()
        real_value = int(tmp[2:] + tmp[:2],16)
        result.append(real_value)

    framecnt = 50
    framecnt = -1

    if(framecnt==0):
        framecnt = 50
        tmp = ser.read(10000).hex()

