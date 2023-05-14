import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)

try:
    while True:
        if (GPIO.input(22)==0):
            print("Button 1 pressed")
            time.sleep(0.3)

        elif (GPIO.input(23)==0):
            print("Button 2 pressed")
            time.sleep(0.3)

        else:
            print("no button pressed")
            time.sleep(0.3)

except KeyboardInterrupt:
  print(" Interrupted")
  GPIO.cleanup()