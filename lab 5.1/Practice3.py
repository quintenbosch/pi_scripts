import RPi.GPIO as GPIO
import time
# to use raspberry pi GPIO numbers
GPIO.setmode(GPIO.BCM)

def blink(pin1, pin2, pin3, pin4):
  # setup GPIO output channel
  GPIO.setup(pin1, GPIO.OUT)
  GPIO.setup(pin2, GPIO.OUT)
  GPIO.setup(pin3, GPIO.OUT)
  GPIO.setup(pin4, GPIO.OUT)
  GPIO.output(pin1, 1)
  time.sleep(0.1)
  GPIO.output(pin1, 0)
  time.sleep(0.1)
  GPIO.output(pin2, 1)
  time.sleep(0.1)
  GPIO.output(pin2, 0)
  time.sleep(0.1)
  GPIO.output(pin3, 1)
  time.sleep(0.1)
  GPIO.output(pin3, 0)
  time.sleep(0.1)
  GPIO.output(pin4, 1)
  time.sleep(0.1)
  GPIO.output(pin4, 0)
  time.sleep(0.1)

# main program blink GPIO18(pin12) 10 times
for i in range(0,10):
  blink(17, 27, 22, 23)

# cleanup
GPIO.cleanup()
print("Program executed!")