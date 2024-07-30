import RPi.GPIO as GPIO
import time

"""
Class represents an RC circuit where the resistor is a light dependent 
resistor and a 1uF capacitor, and it can be used to detect the amount of 
light prevalent. Moreover, a GPIO pin is used in the circuit to act as 
a switch for discharging and charging the capacitor. Class attributes 
are observer time values for how long the capacitor took to charge up, which can 
be used to detect the amount of light. 

Note: these time values are not universalsince they were obtain in specific 
environment with a certain amount of light. Also, call GPIO.setmode(GPIO.BCM)
before creating an instance of this class.
"""
class LightSensor:
    MIN_RC_TIME = 0.07 #milli-seconds
    MAX_RC_TIME = 340
    RC_TIME_RANGE = MAX_RC_TIME - MIN_RC_TIME

    def __init__(self,pin):
        self.sensor_pin = pin
        self.light_check = 85 #Amount of light flag as a percentage

    #Purpose: Wait for light percentage to be above self.light_check
    def wait_for_light(self):
        light_percent = self.get_percentage()
        time.sleep(0.5)

        while not (light_percent > self.light_check):
            light_percent = self.get_percentage() 
            #time.sleep(0.5)
    
    #Purpose: Wait for light percentage to be bellow self.light_check 
    def wait_for_dark(self):
        light_percent = self.get_percentage()
        time.sleep(0.5)

        while not (light_percent <= self.light_check):
            light_percent = self.get_percentage() 
            #time.sleep(0.5)

    #Purpose: Calculate amount of light present as a percentage 
    #        of RC time scale
    #Return: percentage as an integer
    def get_percentage(self): 
        current_rc_time = self._rc_time()
        
        if current_rc_time < self.MIN_RC_TIME:
            return 100.0
        if current_rc_time > self.MAX_RC_TIME:
            return  0.0

        temp = current_rc_time / self.RC_TIME_RANGE
        light_percent = round((1.0 - temp) * 100 )

        return light_percent
    
    #Purpose: Utility method for determining time taken to 
    #         charge up capacitor in RC circuit
    #Return: Time in milli-seconds
    def _rc_time(self): 
        GPIO.setup(self.sensor_pin,GPIO.OUT)
        GPIO.output(self.sensor_pin,GPIO.LOW)
        time.sleep(0.01)

        GPIO.setup(self.sensor_pin, GPIO.IN)
        start_time = time.time()
        while (GPIO.input(self.sensor_pin) == GPIO.LOW):
            pass

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        return elapsed_time
