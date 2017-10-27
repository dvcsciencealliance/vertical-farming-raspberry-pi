import time
import serial
from Sensor import *

class Arduino:
    BaudRate = 9600

    def __init__(self, specs):
        self.name = specs['name']
        self.port = specs['port']
        self.ser = serial.Serial(self.port, timeout=2)
        self.sensors = [Sensor.makeSensor(s)for s in specs['sensors']]
        self.on = 0


    def read(self):
        self.ser.write(self.getCommand())
        time.sleep(0.2)
        line = self.ser.readline().rstrip()

        result = {}
        for sensor in self.sensors:
            if len(line) > 0:
                data = line.split(b' ')
                result[sensor.name] = sensor.read(data[sensor.pin])
        return result

    def getCommand(self):
        return 1 if self.on else 0
