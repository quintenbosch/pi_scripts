import RPi.GPIO as GPIO
import time
# to use raspberry pi GPIO numbers
GPIO.setmode(GPIO.BCM)

def blink(pin):
  # setup GPIO output channel
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 1)
  time.sleep(0.5)
  GPIO.output(pin, 0)
  time.sleep(0.5)

try:
  while True:
# GPIO pin 1
    blink(1)

except KeyboardInterrupt:
  print(" Interrupted")
  GPIO.cleanup()