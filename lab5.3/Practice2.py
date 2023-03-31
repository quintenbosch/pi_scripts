import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def measure(pin1, pin2):
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.OUT)

    if (GPIO.input(pin1) == GPIO.LOW):
        print("Dark")
        GPIO.output(pin2, 1)
        time.sleep(0.5)
    else:
        print("Light")
        GPIO.output(pin2, 0)
        time.sleep(0.5)

try:
    while True:
        measure(17,27)

except KeyboardInterrupt:
    GPIO.cleanup()
    print(" Interrupted")