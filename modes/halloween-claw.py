#!/usr/bin/env python3
import logging
import threading
from time import sleep
from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.led import Leds
from ev3dev.ev3 import Sound

STOP = False

logging.getLogger().setLevel(logging.INFO)

opts = '-a 200 -s 110 -v'
Sound.speak("Mua ha ha ha", espeak_opts=opts+'en+us').wait()

fingers_motor = LargeMotor(OUTPUT_A)
wrist_motor = LargeMotor(OUTPUT_B)
eyes = UltrasonicSensor(INPUT_4)

logging.info('Powering up! Go claw!')
while True:
  if eyes.distance_centimeters <= 10:
    Sound.play('../sounds/laugh.wav')
    wrist_motor.on_for_degrees(SpeedPercent(60), 80)
    fingers_motor.on_for_degrees(SpeedPercent(60), 30)
    fingers_motor.on_for_degrees(SpeedPercent(60), -10)
    fingers_motor.on_for_degrees(SpeedPercent(60), 20)
    # reset
    wrist_motor.on_for_degrees(SpeedPercent(60), -80)
    fingers_motor.on_for_degrees(SpeedPercent(60), -40)

"""
def thread_main():
  while not STOP:
    Sound.play('../sounds/LaughingWitch.wav').wait()


thread = threading.Thread(target=thread_main)
thread.start()
# other code
STOP = True
thread.join()"""