import cgitb ; cgitb.enable()
import spidev
import time
import busio
import digitalio
import board
import RPi.GPIO as GPIO
from adafruit_bus_device.spi_device import SPIDevice

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs0 = digitalio.DigitalInOut(board.CE0)
adc = SPIDevice(spi, cs0, baudrate=1000000)


def readadc(adcnum):
    if ((adcnum>7) or (adcnum<0)):
        return -1
    with adc:
        r=bytearray(3)
        spi.write_readinto([1,(8+adcnum)<<4,0],r)
        time.sleep(0.000005)
        adcout=((r[1]&3)<<8) + r[2]
        return adcout
    
try:
    while True:
        tmp0 = readadc(0)
        if tmp0 < 511:
            GPIO.output(17, 1)
            GPIO.output(18, 0)
        else:
            GPIO.output(17, 0)
            GPIO.output(18, 1)
        print ("input0:",tmp0)
        time.sleep(0.2)
except KeyboardInterrupt:
    print (" Interrupted")
    GPIO.cleanup()        