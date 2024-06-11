from pinpong.board import Board,Pin
import time

def blink(led):
    global blink_on_time, blink_off_time, led_status, last_change, blink_status
    now_time = time.time()
    if blink_status:
        if (not led_status and now_time - last_change > blink_off_time)\
              or (led_status and now_time - last_change > blink_on_time):
            led_status = not led_status 
            led.value(led_status)
            last_change = now_time

b = Board("uno").begin()
led = Pin(Pin.D13, Pin.OUT)
but_status = 0
but = Pin(7, Pin.IN)
led_status = 0
blink_on_time = 0.2
blink_off_time = 1
last_change = 0
blink_status = True
while True:
    val = but.value()
    blink(led)
    if val != but_status:
        print(val)
        but_status = val
        if val == 1:
            blink_status = not blink_status
