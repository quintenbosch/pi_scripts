import RPi.GPIO as GPIO
import time
# to use raspberry pi GPIO numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.IN)

def blink(pin1):
  # setup GPIO output channel
  GPIO.setup(pin1, GPIO.OUT)
  GPIO.output(pin1, 1)
  time.sleep(0.5)
  GPIO.output(pin1, 0)
  time.sleep(0.5)
  GPIO.output(pin1, 1)
  time.sleep(1.5)
  GPIO.output(pin1, 0)
  time.sleep(0.5)
  GPIO.output(pin1, 1)
  time.sleep(0.5)

try:
  while True:
    if (GPIO.input(2)==1):
      blink(1)
    else:
      GPIO.output(1, 0)

except KeyboardInterrupt:
  print(" Interrupted")
  GPIO.cleanup()