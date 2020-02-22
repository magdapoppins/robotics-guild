#!/usr/bin/env python3

from ev3dev2.display import Display
from textwrap import wrap
from time import sleep

from PIL import Image, ImageDraw, ImageFont, ImageFilter

lcd = Display()

def show_text(string, font_name='courB24', font_width=15, font_height=24):
    lcd.clear()
    strings = wrap(string, width=int(180/font_width))
    for i in range(len(strings)):
        x_val = 89-font_width/2*len(strings[i])
        y_val = 63-(font_height+1)*(len(strings)/2-i)
        lcd.text_pixels(strings[i], False, x_val, y_val, font=font_name)
    lcd.update()

# def show_eyes(image):
#     lcd.clear()
#     lcd.image.paste(image, (0, 0))
#     lcd.update()


# image = Love.bmp
# show_eyes()
# sleep(2)


unicode_font = ImageFont.truetype("DejaVuSansMono-Bold.ttf", 36)

# face = u'\u0CA0\uFF3F\u0CA0'
face = 'ಠ_ಠ'
show_text(face, unicode_font, 9, 14)
sleep(10)
