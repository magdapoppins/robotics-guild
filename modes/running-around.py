#!/usr/bin/env python3
from time import sleep
from ev3dev.ev3 import *
from ev3dev2.led import Leds
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedRPM, MoveTank
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_3, INPUT_4, INPUT_2
from ev3dev2.button import Button
import logging
import random

leds = Leds()

logging.getLogger().setLevel(logging.INFO)

logging.info('Connecting motors')
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
# One left and one right motor should be connected

monty_pythonisms = [
  "What are you gonna do, bleed on me?",
  "Ask me the questions, bridgekeeper. I am not afraid.",
  "I dont know that. Aaaaaaaaagh!",
  "I think it was, blessed are the cheesemakers.",
  "Well, what are you doing creeping around a cow shed at two oclock in the morning? That doesnt sound very wise to me",
  "Well, spam, egg, sausage, and spam - thats not got much spam in it.",
  "Your mother was a hamster and your father smelt of elderberries.",
  "I fart in your general direction.",
  "Go and boil your bottoms, sons of a silly person.",
   "You don't frighten us, English pig-dogs!",
   "No, now go away or I shall taunt you a second time-a!"
]

baarihuuto = [
  'perkele',
  'jumalauta',
  'haluutko turpiin',
  'torille',
  'maksalaatikko'
]

# Connect color and touch sensors and check that they
# are connected.
logging.info('Connecting sensors')
us = UltrasonicSensor(INPUT_2)
ts = TouchSensor(INPUT_3)

opts = '-a 200 -s 110 -v'

#leds.animate_cycle('RED', 'GREEN', 'AMBER', 'BLACK', 'ORANGE', 'YELLOW')
#leds.animate_cycle('GREEN', 'AMBER', 'ORANGE', 'YELLOW')

logging.info('Powering up! Lets go!')
while True:
  logging.info('ultrasonic: ' + str(us.distance_centimeters)) # TODO turn when under 30cm
  if us.distance_centimeters <= 10 or ts.is_pressed:
    direction = random.choice(range(1, 2))
    roll = random.randrange(100, 500)
    right_turn = roll if direction == 1 else -(roll)
    left_turn = roll if direction == 2 else -(roll)
    right_motor.run_timed(time_sp=1000, speed_sp=right_turn)
    left_motor.run_timed(time_sp=1000, speed_sp=left_turn)
    Sound.speak(random.choice(baarihuuto), espeak_opts=opts+'fi').wait()
  right_motor.run_forever(speed_sp=100)
  left_motor.run_forever(speed_sp=100)
  #else:
    #leds.animate_cycle('GREEN', 'AMBER', 'ORANGE', 'YELLOW')
