#!/usr/bin/env python

from random import randint

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = False


print("""Random Sparkles

Displays random, colorful sparkles.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

width = 8
height = 8

while True:
    x = randint(0, (width-1))
    y = randint(0, (height-1))
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
