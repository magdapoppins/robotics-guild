#!/usr/bin/env python3
from time import sleep
from ev3dev2.led import Leds
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedRPM, MoveTank
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_3, INPUT_4, INPUT_2
from ev3dev2.button import Button
import logging

leds = Leds()

logging.getLogger().setLevel(logging.INFO)

logging.info('Connecting motors')
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
# One left and one right motor should be connected

# Connect color and touch sensors and check that they
# are connected.
logging.info('Connecting sensors')
us = UltrasonicSensor(INPUT_2)

#leds.animate_cycle('RED', 'GREEN', 'AMBER', 'BLACK', 'ORANGE', 'YELLOW')
#leds.animate_cycle('GREEN', 'AMBER', 'ORANGE', 'YELLOW')

logging.info('Powering up! Lets go!')
while True:
  logging.info('ultrasonic: ' + str(us.distance_centimeters)) # TODO turn when under 30cm
  right_motor.run_forever(speed_sp=100)
  left_motor.run_forever(speed_sp=100)
  #else:
    #leds.animate_cycle('GREEN', 'AMBER', 'ORANGE', 'YELLOW')
