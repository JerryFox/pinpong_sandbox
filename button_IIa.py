from pinpong.board import Board,Pin
b = Board("uno").begin()
led = Pin(13, Pin.OUT)
but = Pin(7, Pin.IN)
but_status = 0
led_status = 0
while True:
    val = but.value()
    if val != but_status: 
        print(val)
        but_status = val
        if val: 
            led_status = not led_status
            led.value(led_status)