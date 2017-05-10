import struct
import math
class Sensor:
    # Member variables
    type = ''
    name = ''
    pin = ''

    # Member functions
    def __init__(self, str):
        specs = str.split(' ')
        [self.type, self.name, self.pin] = [specs[0], specs[1], int(specs[2])]

    def read(self, data):
        value = int(data)
        result = {
        'temperature': self.temperature,
        'ph': self.ph,
        }[self.type](value)
        return result

    def temperature(self, value):
        count = float(value)
        resistor = 15000.0
        resistance = (resistor * count / (1024.0 - count))
        logResistance = math.log(resistance)
        tempInKelvin = 1.0 / (0.00102119 + (0.000222468 * logResistance) + (0.000000133342 * pow(logResistance, 3)))
        tempInCelsius = tempInKelvin - 273.15
        return tempInCelsius

    def ph(self, value):
        count = float(value)
        slope = -3.838
        intercept = 13.720
        voltage = count / 1023 * 5.0
        ph = intercept + voltage * slope
        return ph