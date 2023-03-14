import RPi.GPIO as GPIO
import time
# to use raspberry pi GPIO numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def blink(pin1, pin2):
  # setup GPIO output channel
  GPIO.output(pin1, 1)
  GPIO.output(pin2, 1)
  time.sleep(0.5)
  GPIO.output(pin1, 0)
  GPIO.output(pin2, 0)
  time.sleep(0.5)


try:
   while True:
      if (GPIO.input(2)==1):
# GPIO pin 1
        blink(1, 17)
        print("Led blinks")
      else:
        GPIO.output(1, 0)
        GPIO.output(17, 0)
        print("Led not flashing")
        time.sleep(1)

except KeyboardInterrupt:
  print(" Interrupted")
  GPIO.cleanup()