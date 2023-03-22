import cgitb ; cgitb.enable()
import spidev
import time
import busio
import digitalio
import board
import requests
from adafruit_bus_device.spi_device import SPIDevice
url = "http://quintenb.hub.ubeac.io/iotessquintenbosch"
uid = "iotessquintenbosch"
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
        tmp0 = readadc(0)/10
        tmp1 = readadc(1)
        data = {
            "id": uid,
            "sensors":[
            {
            'id': 'adc kanaal0',
            'data': tmp0
            },
            {
            'id': 'adc kanaal1',
            'data': tmp1
            }]
        }
        r = requests.post(url, verify=False, json=data)
        print ("input0:",tmp0)
        print("input1:",tmp1)
        time.sleep(1)
except KeyboardInterrupt:
    print (" Interrupted")       