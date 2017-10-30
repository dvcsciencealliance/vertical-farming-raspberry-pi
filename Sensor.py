import math
from abc import ABC, abstractmethod

class Sensor(ABC):
    # Member variables
    type = ''
    name = ''
    pin = ''

    # Member functions
    def __init__(self, specs):
        self.type, self.name, self.pin = specs['type'], specs['name'], int(specs['pin'])

    def makeSensor(specs):
        return {
        'temperature': TemperatureSensor,
        'ph': PhSensor,
        'conductivity': ConductivitySensor
        }[specs['type']](specs)

    @abstractmethod
    def read(self, data):
        pass

class TemperatureSensor(Sensor):
    def read(self, value):
        count = float(value)
        resistor = 15000.0
        resistance = (resistor * count / (1024.0 - count))
        logResistance = math.log(resistance)
        tempInKelvin = 1.0 / (0.00102119 + (0.000222468 * logResistance) + (0.000000133342 * pow(logResistance, 3)))
        tempInCelsius = tempInKelvin - 273.15
        return tempInCelsius

class PhSensor(Sensor):
    def read(self, value):
        count = float(value)
        slope = -3.838
        intercept = 13.720
        voltage = count / 1023 * 5.0
        ph = intercept + voltage * slope
        return ph

class ConductivitySensor(Sensor):
    def read(self, value):
        count = float(value)
        slope = 967
        intercept = 0
        voltage = count / 1023 * 5.0
        result = intercept + voltage * slope
        return result