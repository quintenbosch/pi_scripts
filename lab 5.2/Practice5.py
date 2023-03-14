import RPi.GPIO as GPIO
import time
# to use raspberry pi GPIO numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)

def blinkright(pin1, pin2, pin3, pin4):
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

def blinkleft(pin1, pin2, pin3, pin4):
  GPIO.setup(pin1, GPIO.OUT)
  GPIO.setup(pin2, GPIO.OUT)
  GPIO.setup(pin3, GPIO.OUT)
  GPIO.setup(pin4, GPIO.OUT)

  GPIO.output(pin4, 1)
  time.sleep(0.1)
  GPIO.output(pin4, 0)
  time.sleep(0.1)
  GPIO.output(pin3, 1)
  time.sleep(0.1)
  GPIO.output(pin3, 0)
  time.sleep(0.1)
  GPIO.output(pin2, 1)
  time.sleep(0.1)
  GPIO.output(pin2, 0)
  time.sleep(0.1)
  GPIO.output(pin1, 1)
  time.sleep(0.1)
  GPIO.output(pin1, 0)
  time.sleep(0.1)

try: 
  while True:
    if (GPIO.input(2)==1):
      blinkright(17,27,22,23)
    else:
      blinkleft(17,27,22,23)

except KeyboardInterrupt:
  print(" Interrupted")
  GPIO.cleanup()