#!/usr/bin/env python3

import time
import random
from ev3dev.ev3 import *

#Sound.tone(1500, 2000).wait()

#https://www.wavsource.com/
# Sound.play('../sounds/rubber_ducky.wav').wait()
# sleep(10)


# Sound.tone(100, 2000).wait()
# time.sleep(1)
# Sound.tone(6500, 2000).wait()
# time.sleep(1)
# Sound.tone(500, 2000).wait()
# Sound.tone(2500, 2000).wait()
# Sound.tone(1500, 2000).wait()
#Sound.tone([(200, 2000, 400),(800, 1000, 3000)])

# Sound.play_song((
#  ('D4', 'e3'),      # intro anacrouse
#  ('D4', 'e3'),
#  ('D4', 'e3'),
#  ('G4', 'h'),       # meas 1
#  ('D5', 'h'),
#  ('C5', 'e3'),      # meas 2
#  ('B4', 'e3'),
#  ('A4', 'e3'),
#  ('G5', 'h'),
#  ('D5', 'q'),
#  ('C5', 'e3'),      # meas 3
#  ('B4', 'e3'),
#  ('A4', 'e3'),
#  ('G5', 'h'),
#  ('D5', 'q'),
#  ('C5', 'e3'),      # meas 4
#  ('B4', 'e3'),
#  ('C5', 'e3'),
#  ('A4', 'h')
# ))

#Sound.play('../sounds/hello.wav').wait()

monty_pythonisms = [
  "What are you gonna do, bleed on me?",
  "Ask me the questions, bridgekeeper. I am not afraid.",
  "I don’t know that. Aaaaaaaaagh!",
  "I think it was, ‘blessed are the cheesemakers’.",
  "Well, what are you doing creeping around a cow shed at two o’clock in the morning? That doesn’t sound very wise to me",
  "Well, spam, egg, sausage, and spam – that’s not got much spam in it."
]
opts = '-a 200 -s 110 -v'

Sound.speak(random.choice(monty_pythonisms), espeak_opts=opts+'en+whisper').wait()


#print('YEET')

#Sound.speak('Hello, my name is Potato')
time.sleep(1)

str_en = 'I am gonna take my horse to the old town road'
str_fr = "Ceci c'est pas une pipe"
str_whisper = 'Fuck the police'
str_ru = 'Menya zovut kartoshka'

# male high voice
#print('Man')
#Sound.speak(str_en)
# female high voice
print('american lady')
#Sound.speak(str_en, espeak_opts=opts+'en+us').wait()

# print('Popo hater')
# Sound.speak(str_whisper, espeak_opts=opts+'en+whisper').wait()

# print('asd')
# #Sound.speak(str_en, espeak_opts=opts+'en+f5').wait()

# print('Russian')
# Sound.speak(str_ru, espeak_opts=opts+'ru+m5').wait()

# print('asd')
# Sound.speak(str_fr, espeak_opts=opts+'fr+f5').wait()

#time.sleep(2)
#print('Playing magic wand sound')
#Sound.play('/home/robot/sounds/magic_wand.wav')




#https://sites.google.com/site/ev3devpython/learn_ev3_python/sound