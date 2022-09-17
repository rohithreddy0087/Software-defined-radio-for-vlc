#PYTHON CODE FOR RASPBERRY PI
import serial
ser = serial.Serial('/dev/ttyACM2', 9600)
mak='1111111111'
d ='01010101010101010101'
d=mak+d+d+d+d+d[0:10]
a=bin(158974558446*(12**30))
a=a[2:len(a)]
print(len(d))
data=d.encode()
ser.write(data)
