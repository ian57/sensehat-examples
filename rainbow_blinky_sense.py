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
sense.set_rotation(0)
sense.low_light = False


print("""Rainbow Blinky

Blinks a rainbow from the center of the display.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

width = 8
height = 8

if height==width:
    delta=0
else:
    delta=2


def make_gaussian(fwhm):
    x = numpy.arange(0, 8, 1, float)
    y = x[:, numpy.newaxis]
    x0, y0 = 3.5, 3.5
    fwhm = fwhm
    gauss = numpy.exp(-4 * numpy.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss

while True:
    for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
        fwhm = 5.0/z
        gauss = make_gaussian(fwhm)
        start = time.time()
        for y in range(height):
            for x in range(width):
                h = 1.0/(x + y + delta + 1)
                s = 0.8
                if height<=width:
                    v = gauss[x,y+delta]
                else:
                    v = gauss[x+delta,y]
                rgb = colorsys.hsv_to_rgb(h, s, v)
                r = int(rgb[0]*255.0)
                g = int(rgb[1]*255.0)
                b = int(rgb[2]*255.0)
                sense.set_pixel(x, y, r, g, b)
        end = time.time()
        t = end - start
        if t < 0.04:
            time.sleep(0.04 - t)
