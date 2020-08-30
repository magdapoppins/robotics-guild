#!/usr/bin/env python3

import time
from ev3dev.ev3 import *

#Sound.tone(1500, 2000).wait()

#https://www.wavsource.com/
Sound.play('../sounds/rubber_ducky.wav').wait()
sleep(10)
Sound.play('../sounds/seal.wav').wait()

#Sound.play('../sounds/hello.wav').wait()
