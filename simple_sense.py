#!/usr/bin/env python

import time

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.low_light = False


width = 8
height = 8

sense.clear()

while (True):
	for y in range(height):
	  for x in range(width):
	    sense.set_pixel(x,y,255,0,255)
	    time.sleep(0.05)

	for y in range(height):
	  for x in range(width):
	    sense.set_pixel(x,y,0,0,0)
	    time.sleep(0.05)
time.sleep(1)
