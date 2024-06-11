from pinpong.board import Board,Pin
import time

def blink(l):
    now_time = time.time()
    if l["blink_status"]:
        if (not l["led_status"] and now_time - l["last_change"] > l["blink_off_time"])\
              or (l["led_status"] and now_time - l["last_change"] > l["blink_on_time"]):
            l["led_status"] = not l["led_status"] 
            l["led"].value(l["led_status"])
            l["last_change"] = now_time

b = Board("uno").begin()
led1 = {}
led1["led"] = Pin(Pin.D13, Pin.OUT)
led1["led_status"] = 0
led1["blink_on_time"] = 0.2
led1["blink_off_time"] = 1
led1["last_change"] = 0
led1["blink_status"] = True
but = Pin(7, Pin.IN)
but_status = 0
while True:
    val = but.value()
    blink(led1)
    if val != but_status:
        print(val)
        but_status = val
        if val == 1:
            led1["blink_status"] = not led1["blink_status"]
