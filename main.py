import Arduino
import time
import Database

db = Database.Database()

cfgdir = 'config/'
fmaincfg = open(cfgdir + 'main.cfg', 'r')

arduinos = []
n = int(fmaincfg.readline())
for i in range(0, n):
    arduinos.append(Arduino.Arduino(fmaincfg.readline().rstrip()))

while True:
    for arduino in arduinos:
        data = arduino.read()
        db.insert(data, arduino.name)
    time.sleep(3)
