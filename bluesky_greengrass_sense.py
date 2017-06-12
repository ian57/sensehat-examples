#!/usr/bin/env python

import time

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.low_light = True
width = 8
height = 8

print("""Blue Sky, Green Grass

Displays a horizon on your Unicorn HAT/pHAT so you can
see which orientation is which.

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

sense.clear()

y=0
for x in range(width):
  sense.set_pixel(x,y,0,255,0)
  time.sleep(0.05)

y=height-1
for x in range(width):
  sense.set_pixel(x,y,0,0,255)
  time.sleep(0.05)

for y in range(1,3):
  for x in range(0,y):
    sense.set_pixel(x,y,255,0,0)
    time.sleep(0.05)

time.sleep(10)
