import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


def measure(pin1, pin2):
  while True:
    GPIO.output(pin1, 1)
    time.sleep(0.00001)
    GPIO.output(pin1, 0)
    while (GPIO.input(pin2) == 0):
        pass
    signaalhigh = time.time()
    while (GPIO.input(pin2) == 1):
        pass
    signaallow = time.time()
    timepassed = signaallow - signaalhigh
    distance = round(timepassed * 17000, 2)
    return distance

def turn(pin1, pin2, pin3, pin4):
  GPIO.output(pin1, 1)
  time.sleep(0.01)
  GPIO.output(pin1, 0)
  GPIO.output(pin2, 1)
  time.sleep(0.01)
  GPIO.output(pin2, 0)
  GPIO.output(pin3, 1)
  time.sleep(0.01)
  GPIO.output(pin3, 0)
  GPIO.output(pin4, 1)
  time.sleep(0.01)
  GPIO.output(pin4, 0)

try:
   while True:
      waterlevel = measure(26,16)
      if waterlevel > 30:
        print("Safe")
        print(waterlevel, "cm")
        time.sleep(5)
      else:
        print("Alarm")
        print(waterlevel, "cm")
        for i in range(100):
           turn(17,27,22,23)

except KeyboardInterrupt:
   print(" Program interrupted")
   GPIO.cleanup()