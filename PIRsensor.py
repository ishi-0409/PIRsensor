import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
motion=18
LED=21
GPIO.setup(motion,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
sleep(10)
try:
    while True:
        motionval=GPIO.input(motion)
        print(motionval)
        if motionval==0:
            GPIO.output(LED,GPIO.LOW)
        if motionval==1:
            GPIO.output(LED,GPIO.HIGH)   
        sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
