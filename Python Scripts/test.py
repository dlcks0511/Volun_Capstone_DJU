import serial

port= "COM4"
baudrate=9600
ser = serial.Serial(port,9600)


ser.write(b"Hello arduino!")

data = ser.readline()
print(data)

ser.close()
