import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)

try:
    while True:
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, 0)
        time.sleep(0.1)

        GPIO.setup(18, GPIO.IN)
        starttime = datetime.datetime.now()
        while(GPIO.input(18)==0):
            pass
        stoptime = datetime.datetime.now()
        interval = (stoptime - starttime)
        print(interval.microseconds)

except KeyboardInterrupt:
    GPIO.cleanup()
    print(" Interrupted")