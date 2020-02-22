from ev3dev2.display import Display

import random

display = Display()

def circles():
  while True:
    display.circle(random.randint(10, 100))
    sleep(10)