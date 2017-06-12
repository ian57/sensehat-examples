#!/usr/bin/env python

import colorsys
import time
from sys import exit

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = False


print("""Random Blinky

Blinks random yellow-orange-red LEDs.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

width = 8
height = 8


while True:
    rand_mat = numpy.random.rand(width,height)
    for y in range(height):
        for x in range(width):
            h = 0.1 * rand_mat[x, y]
            s = 0.8
            v = rand_mat[x, y]
            rgb = colorsys.hsv_to_rgb(h, s, v)
            r = int(rgb[0]*255.0)
            g = int(rgb[1]*255.0)
            b = int(rgb[2]*255.0)
            sense.set_pixel(x, y, r, g, b)
    time.sleep(0.01)
