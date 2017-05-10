import serial
import time
import Sensor

class Arduino:
    name = ''
    cfgdir = 'config/'
    port = ''
    BaudRate = 9600
    sensors = []
    ser = serial.Serial()

    def __init__(self, filename):
        fcfg = open(self.cfgdir + filename)
        self.name = filename[:-4]
        self.port = fcfg.readline().rstrip()
        self.ser = serial.Serial(self.port, timeout=2)
        numSensors = int(fcfg.readline().rstrip())
        for i in range(0, numSensors):
            self.sensors.append(Sensor.Sensor(fcfg.readline().rstrip()))

    def read(self):
        self.ser.write(1)
        time.sleep(0.2)
        line = self.ser.readline().rstrip()


        result = {}
        for sensor in self.sensors:
            if len(line) > 0:
                print(line)
                data = line.split(b' ')
                print(data)
                result[sensor.name] = sensor.read(data[sensor.pin])

        return result