import RPi.GPIO as GPIO

"""
Class switches a laser diode off and on using an NPN transistor.
Note: call GPIO.setmode(GPIO.BCM) before creating an instance for this class.  
"""
class Laser:
    def __init__(self,pin):
        self.laser_pin = pin
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    #Apply voltage to base of NPN transistor
    def on(self):
        GPIO.output(self.laser_pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.laser_pin, GPIO.LOW)
