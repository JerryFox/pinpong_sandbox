from pinpong.board import Board,Pin
b = Board("uno").begin()
led = Pin(13, Pin.OUT)
but = Pin(7, Pin.IN)
but_status = 0
while True:
    val = but.value()
    if val != but_status: 
        led.value(val)
        print(val)
        but_status = val
