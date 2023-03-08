import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

try:
    while True:
        GPIO.output(17, 1)
        time.sleep(0.00001)
        GPIO.output(17, 0)
        while (GPIO.input(18) == 0):
            pass
        signaalhigh = time.time()
        while (GPIO.input(18) == 1):
            pass
        signaallow = time.time()
        timepassed = signaallow - signaalhigh
        distance = round(timepassed * 17000, 2)
        print(distance, "cm")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print(" Interrupted")