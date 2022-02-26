import time
import serial


def SerialOpen():
    try:
        ser = serial.Serial(
            port='\\\\.\\COM5',
            baudrate=115200,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        if ser.isOpen():
            ser.close()
        ser.open()
        ser.isOpen()
        return ser
    except Exception as e:
        print(e)


def sendData(ser, data):
    try:
        ser.flushInput()
        ser.flushOutput()
        # ser.write("GUI@A\r".encode())
        ser.write(data.encode())
        time.sleep(1)
    except Exception as e:
        print(e)


def getData(ser):
    try:
        out = ''
        max = 211
        count = 0
        # ser.flushOutput()
        # while True:
        if ser.inWaiting() > 0:
            values = ser.read(ser.inWaiting())
        out = values.decode('utf8')
            # values = ser.readline().decode('utf8')
            # count+=1
            # if values != b'':
            #     out += values.decode('utf8')
            # else:
            #     break
            # if count >= max:
            #     break

        if out != '':
            print(">>" + out)
        # return out

    except Exception as e:
        print(e)

ser = SerialOpen()
if ser.inWaiting() > 0:
    values = ser.read(ser.inWaiting())
else:
    print('wait')
# sendData(ser, "GUI@\r")
time.sleep(.1)
sendData(ser, "GS\r")
sendData(ser, "QH\r")
sendData(ser, "X\r")
sendData(ser, "A\r")
time.sleep(.1)
getData(ser)
time.sleep(.1)
sendData(ser, "GS\r")
sendData(ser, "OP\r")
sendData(ser, "X\r")
sendData(ser, "A\r")
time.sleep(.1)
getData(ser)

ser.close()

