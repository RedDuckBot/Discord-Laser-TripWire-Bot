import RPi.GPIO as GPIO
from laser import Laser
from light_sensor import LightSensor

"""Program used to test laser and light sensor circuits"""

GPIO.setmode(GPIO.BCM)
laser = Laser(27)
light_sensor = LightSensor(17)

while True:
    cmd = input("Enter cmd: ")

    if cmd == "0": 
        laser.on()
    elif cmd == "1":
        laser.off()
    elif cmd == "2":
        print("waiting...")
        light_sensor.wait_for_dark()
        print("Done")
    elif cmd == "3":
        break
    else:
        print("Not valid cmd.")

GPIO.cleanup()






