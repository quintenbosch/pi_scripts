import RPi.GPIO as GPIO
import time
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

try:
  while True:
      if (GPIO.input(2)==1):
          print("button pressed")
          GPIO.output(18,1)
          GPIO.output(17,0)
          time.sleep(0.3)
      else:
          GPIO.output(18,0)
          GPIO.output(17,1)
          print("button released")
          time.sleep(0.3)

except KeyboardInterrupt:
    print(" Interrupted")
    GPIO.cleanup()