import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def turn(pin1, pin2, pin3, pin4):
  GPIO.setup(pin1, GPIO.OUT)
  GPIO.setup(pin2, GPIO.OUT)
  GPIO.setup(pin3, GPIO.OUT)
  GPIO.setup(pin4, GPIO.OUT)

  GPIO.output(pin1, 1)
  GPIO.output(pin2, 1)
  time.sleep(1)
  GPIO.output(pin1, 0)
  GPIO.output(pin2, 1)
  GPIO.output(pin3, 1)
  time.sleep(1)
  GPIO.output(pin2, 0)
  GPIO.output(pin3, 1)
  GPIO.output(pin4, 1)
  time.sleep(1)
  GPIO.output(pin3, 0)
  GPIO.output(pin4, 1)
  GPIO.output(pin1, 1)
  time.sleep(1)
  GPIO.output(pin4, 0)

#for i in range(0,5):
try:
  while True:
    turn(7,8,25,24)

except KeyboardInterrupt:
  print(" Interrupted")
  GPIO.cleanup()
