import serial
import time
port = 'COM3'
BaudRate = 9600
ser = serial.Serial(port)

time.sleep(5)

stuff = input('Say something to RPI: ')
while stuff != '//':
    ser.write(stuff.encode('UTF-8'))
    stuff = input('Say something to RPI: ')

while True:
    str = ser.readline()
    data = str.split(b' ')
    print(str)