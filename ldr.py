import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def measure(pin1,pin2):
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.OUT)

    if (GPIO.input(pin1) == GPIO.LOW):
        print("Dark")
        time.sleep(0.5)
        GPIO.output(pin2, 1)
    else:
        print("Light")
        time.sleep(0.5)
        GPIO.output(pin2, 0)

try:
    while True:
        measure(17,18)

except KeyboardInterrupt:
    GPIO.cleanup()
    print(" Interrupted")