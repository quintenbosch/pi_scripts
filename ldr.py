import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def measure(pin1):
    GPIO.setup(pin1, GPIO.IN)

    if (GPIO.input(pin1) == GPIO.LOW):
        print("Dark")
        time.sleep(0.5)
    else:
        print("Light")
        time.sleep(0.5)

try:
    while True:
        measure(17)

except KeyboardInterrupt:
    GPIO.cleanup()
    print(" Interrupted")