import time
from machine import Pin
import sys
from mfrc522 import MFRC522

led_red = Pin(14, machine.Pin.OUT)
led_green = Pin(13, machine.Pin.OUT)
led_blue= Pin(12, machine.Pin.OUT)
led_green.value(0)
led_red.value(0)
led_blue.value(0)
reader = MFRC522(spi_id=0,sck=2,mosi=3,miso=4,cs=5,rst=0)

def toggle(obj):
        obj.value(1)
        time.sleep(0.5)
        obj.value(0)
print("OK")
reader.init()
while True:
    # read a command from the host
    v = sys.stdin.readline().strip()
    if v.lower() == "on":
        led_blue.value(1)
        time.sleep(1)
        print("...attiva")
    elif v.lower() == "ok":
        toggle(led_green)
    elif v.lower()=="no":
        toggle(led_red)
    else:
        print("Not found")
############################################################        
    (status, tag_type) = self.reader.request(self.reader.REQIDL)
    if status == self.reader.OK:
       print("Scheda rilevata")
       (status, uid) = self.reader.anticoll()
       if status == self.reader.OK:
          print("UID della scheda:", uid)