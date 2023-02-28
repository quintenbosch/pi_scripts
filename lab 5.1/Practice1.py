import RPi.GPIO as GPIO
import time
# to use raspberry pi GPIO numbers
GPIO.setmode(GPIO.BCM)

try:
  while True:
# GPIO pin 1
    GPIO.setup(1, GPIO.OUT)
    GPIO.output(1, 1)
    time.sleep(1)
    GPIO.output(1, 0)
    time.sleep(1)

except KeyboardInterrupt:
  print("Interrupted")
  GPIO.cleanup()