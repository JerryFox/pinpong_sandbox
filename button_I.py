from pinpong.board import Board,Pin
b = Board("uno").begin()
led = Pin(13, Pin.OUT)
but = Pin(7, Pin.IN)
import time
while True:
   val = but.value()
   led.value(val)
   print(val)