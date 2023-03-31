import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def measure(pin1, pin2, pin3):
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.IN)

    if (GPIO.input(pin1) == GPIO.LOW) or (GPIO.input(pin3) == GPIO.HIGH):
        GPIO.output(pin2, 1)
        print("Light on")
        time.sleep(0.5)
    else:
        GPIO.output(pin2, 0)
        time.sleep(0.5)

try:
    while True:
        measure(17,27,22)

except KeyboardInterrupt:
    GPIO.cleanup()
    print(" Interrupted")