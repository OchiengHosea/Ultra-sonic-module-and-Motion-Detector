import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO_ECHO = 24
GPIO_TRIG = 25
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_TRIG, GPIO.OUT)
def start_monitoring():
    print("Setting up ultrasonic")
    time.sleep(2)
    GPIO.output(GPIO_TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, GPIO.LOW)
    
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        bounce_back_time = time.time()
        
    pulse_duration = bounce_back_time - start_time
    distance = round(pulse_duration*1715, 2)
    print(f"Distance: {distance} cm")