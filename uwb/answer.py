# serial 연결 코드
def connect_serial(port):
    import serial
    ser = serial.Serial(
    port=port,
    baudrate=115200,
    parity=serial.PARITY_NONE,
    ...
    timeout=0
    )
    ser.ser_buffer_size(rx_size=115200, tx_size=115200)
    packet = bytearray()
    packet.append(0x53)#STX1:S
    packet.append(0xf1)#STX2
    packet.append(0x09)#len
    ...
    packet.append(0x4e)#N
    packet.append(0x8B)#CHECKSUM
    packet.append(0x45)#ETX:E
    ser.write(packet)
    return ser

# parsing
    while True:
        stx1 = ser.read(1).hex()
        while (len(stx1) < 1):
            stx1 += ser.read(1-len(stx1)).hex()
        if (stx1 == 'aa'):
            stx2 = ser.read(1).hex()
            while (len(stx2) < 1):
                stx2 += ser.read(1-len(stx2)).hex()
            if (stx1 == '55'):
        ...
        # 1번 방법
        uwb_data = ser.read(10*20)
        while (len(uwb_data) < 10*20):
            uwb_data += ser.read(10*20-len(uwb_data))
        uwb_buffer = np.frombuffer(uwb_data, "<u2")
        
        # 2번 방법
        result = []
        for i in range(10*20):
            tmp = ser.read(2).hex()
            real_value = int(tmp[2:] + tmp[:2] ,16)
            result.append(real_value)
        # 버퍼리셋
        # 버퍼 리셋이 없으면 무분별하게 데이터가 쌓임
            # 정상데이터가 무분별하게 쌓이는거면 속도 조절이 필요하나,
            # 쓰레기 데이터가 쌓여 정상데이터가 안나온다면 문제가 있으니 버퍼 리셋 필수.
        framecnt = 50 # 상단부에 미리선언

        framecnt -= 1
        if (framecnt == 0):
            framecnt = 50
            tmp = ser.read(10000).hex()