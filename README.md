# pinpong_sandbox
## playing with arduino and pinpong python module

- **HW installation**
  > Simply connect arduino board and a computer with USB cabel. OS recognizes new com port.
  > If doesn't there is probably any problem with drivers.
  >
  > *LEDs*
  >
  > You can use internal LED which is connected to port 13 or connect an external LED between any port you want and a ground pin.
  > A serial resistor is not needed because of limited current from arduino ports. 
  >
  > *buttons*
  >
  > I am using non mechanical touch modules in my examples. If you want to use normal mechanical buttons you must remember using
  > internal or external pulldown or [pullup resistor][1].
  >
  > [1]: <https://en.wikipedia.org/wiki/Pull-up_resistor> "pullup resistor"
  >
  
- **SW installation**

  > `pip install pinpong`
  >
  > `pip install ipython` (I like it and usually use it when developing any python code.)
  >
  > `pip list` shows installed modules
  > 
  > If ipython is installed and `ipython` command doesn't work try:
  >
  > `python -m IPython`

- first test
  
  > in python console write:
  >
  > `from pinpong.examples import blink`
  ```console
  >>> from pinpong.examples import blink
  
    __________________________________________
   |    ____  _       ____                    |
   |   / __ \(_)___  / __ \____  ____  ____ _ |
   |  / /_/ / / __ \/ /_/ / __ \/ __ \/ __ `/ |
   | / ____/ / / / / ____/ /_/ / / / / /_/ /  |
   |/_/   /_/_/ /_/_/    \____/_/ /_/\__, /   |
   |   v0.5.2  Designed by DFRobot  /____/    |
   |__________________________________________|
  
  [01] Python3.11.2 Windows-10-10.0.22631-SP0 Board: UNO
  selected -> board: UNO serial: COM6
  [10] Opening COM6
  [32] Firmata ID: 2.8
  [22] Arduino compatible device found and connected to COM6
  [40] Retrieving analog map...
  [42] Auto-discovery complete. Found 20 Digital Pins and 6 Analog Pins
  ------------------------------
  All right. PinPong go...
  ------------------------------
  ```

- using button I
- using button II
- blinkink without delay
- using OOP advantages

