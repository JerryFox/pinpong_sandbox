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
  > I am using non mechanical touch modules in my examples. If you can use normal mechanical buttons you must remember using
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
- using button I
- using button II
- blinkink without delay
- using OOP advantages

