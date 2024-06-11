from pinpong.board import Pin, Board
from curses import wrapper
import time 

def refresh(*args): 
    for i in args: 
        i.refresh()


def main(win, leds=[], buttons=[], loop=None):
    global act_time, window 
    window = win
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key (Enter to end):")
    while 1:
        try:
           key = win.getkey()
           win.addstr(0, 30, str(key) + " " * 10)
           if key == "\n":
              break
        except Exception as e:
           # No input
           pass
        if int(time.time()) != act_time: 
            act_time = int(time.time())
            win.addstr(3, 0, str(act_time))
        for b in buttons: 
            b.refresh()
        for l in leds: 
            l.refresh()
        if loop: 
            loop()


class Led():
    def __init__(self, port):
        self.pin = Pin(port, Pin.OUT)
        self.mode = 0 # 0 - off, 1 - on, 2 - blink
        self.status = 0 # should be ON or OFF
        self.number_of_blinks = -1 # < 0 - endless blinkink   
        self.last_change = 0
        self.blink_on_time = 0.3
        self.blink_off_time = 1

    def on(self): 
        self.pin.value(1)
        self.status = 1

    def off(self): 
        self.pin.value(0)
        self.status = 0

    def blink(self, on_time=0.1, off_time=1, number_of_blinks=-1): 
        self.status = 0
        self.number_of_blinks = number_of_blinks
        self.blink_on_time = on_time
        self.blink_off_time = off_time
        self.last_change = time.time()

    def refresh(self): 
        act_time = time.time()
        if self.mode == 0: 
            if self.status: 
                self.off()
        elif self.mode == 1: 
            if not self.status: 
                self.on()
        elif self.mode == 2 and self.number_of_blinks: 
            if self.status and act_time - self.last_change >= self.blink_on_time:
                self.off()
                self.last_change = act_time
                if self.number_of_blinks > 0: 
                    self.number_of_blinks -= 1
            elif not self.status and act_time - self.last_change >= self.blink_off_time:
                self.on()
                self.last_change = act_time
            

class Button():

    def __init__(self, port) -> None:
        self.pin = Pin(port, Pin.IN)
        self.pressed = 0
        self.last_change = time.time()
        self.double_click = 0
        self.click = 0
        self.click_time_min = 0.05
        self.click_time_max = 0.4
        self.double_click_space_max = 0.4
        self.first_press = 0
        self.second_press = 0
        self.last_press_time = 0
        self.last_release_time = 0
        self.click_before_idle = 0

    def get_pressed(self): 
        gp = self.last_press_time if self.last_press_time > self.last_release_time else 0
        self.last_press_time = 0
        return gp

    def get_released(self): 
        gr = self.last_release_time if self.last_release_time > self.last_press_time else 0
        self.last_release_time = 0
        return gr

    def refresh(self): 
        act_time = time.time()
        val = self.pin.value()
        if val != self.pressed:
            # the button state was changed now
            self.pressed = val
            if self.pressed: 
                # the button was pressed now
                self.last_press_time = act_time
                # is it before idle time - click in sequence
                # is it after idle time - new click
            else: 
                self.last_release_time = act_time
                # what kind of "click" was before? 
                if not self.first_press: 
                    self.first_press = act_time - self.last_press_time
                else: 
                    self.second_press = act_time - self.last_press_time
            self.last_change = act_time
        if not val and act_time - self.last_change >= self.double_click_space_max:
            # accept click (double click) after idle time
            if self.second_press: 
                self.double_click = 1
                self.first_press = 0
                self.second_press = 0
            elif self.first_press: 
                self.click = 1
                self.first_press = 0

    def get_double_click(self):
        dcl = self.double_click
        self.double_click = 0 
        return dcl
    
    def get_click(self):
        cl = self.click
        self.click = 0 
        return cl
    

if __name__ == "__main__":
    act_time = int(time.time())
    b = Board("uno").begin()
    led = Led(13)
    led.number_of_blinks = -1
    but = Button(7)

    def loop(): 
        #global window
        but.refresh()
        led.refresh()
        pressed = but.get_pressed()
        if pressed: 
            window.addstr(1, 0, str(pressed)+"   ")
            led.mode = (led.mode + 1) % 3
        released = but.get_released()
        if released: 
            window.addstr(2, 0, str(released)+"   ")
            #led.mode = (led.mode + 1) % 3

    wrapper(main, loop=loop)
