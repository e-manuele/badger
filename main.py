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
card_db=['2236835850','3111483307','2798319075']
#2798319075
def toggle(obj):
        obj.value(1)
        time.sleep(0.5)
        obj.value(0)
print("OK")

while True:
        toggle(led_blue)      
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid),"little",False)
                if str(card) in card_db:
                    toggle(led_green)
                else:
                    toggle(led_red)
                print(str(card))
                
                
        v = sys.stdin.readline().strip()
        if v.lower() == "..on":
            print("...ok")
        elif v.lower() == ".":
            continue
