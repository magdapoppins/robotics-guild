#!/usr/bin/env python3
import os
from ev3dev2.display import Display
from textwrap import wrap
from time import sleep
import ev3dev2.fonts as fonts
import logging

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedRPM, MoveTank

from PIL import Image, ImageDraw, ImageFont, ImageFilter

logging.getLogger().setLevel(logging.INFO)

# fileDir = os.path.dirname(os.path.realpath('__file__'))
# logging.info(fileDir)
# code_font_path = os.path.join(fileDir, 'assets/CODE2000.ttf')

# Some display docs: https://python-ev3dev.readthedocs.io/en/stable/display.html
lcd = Display()

def show_text(string, font=fonts.load('luBS14'), font_width=15, font_height=24):
    lcd.clear()
    logging.info('Fonts available: {}'.format(fonts.available()))
    lcd.draw.text((font_width, font_height), string, font=font)
    lcd.update()

# https://www.fileformat.info/info/unicode/char/0ca0/index.htm
face = 'ಠ_ಠ'.encode('utf-8')
#show_text(face, ImageFont.truetype(code_font_path, 15), 30, 30) # TODO: fix OSError: cannot open resource
#show_text(face, fonts.load('luBS14'), 30, 30) # TODO: find better default font?

logging.info('Connecting motors')
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
while True:
    right_motor.run_forever(speed_sp=100)

# def show_eyes(image):
#     lcd.clear()
#     lcd.image.paste(image, (0, 0))
#     lcd.update()


# image = Love.bmp
# show_eyes()
# sleep(2)