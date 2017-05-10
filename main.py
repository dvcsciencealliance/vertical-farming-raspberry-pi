import time
import json
import Arduino
import Database

db = Database.Database()

with open('config/main.json') as data_file:
            cfg = json.load(data_file)

arduinos = []
for arduino in cfg['Arduinos']:
    arduinos.append(Arduino.Arduino(arduino))

while True:
    for arduino in arduinos:
        data = arduino.read()
        db.insert(data, arduino.name)
    time.sleep(3)
