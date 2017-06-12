#!/usr/bin/env python

import math
import time

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.low_light = False


print("""Rainbow

Displays a beautiful rainbow across your HAT/pHAT :D

If you're using a Unicorn HAT and only half the screen lights up, 
edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
""")

width = 8
height = 8


#print("Reticulating splines")
#time.sleep(.5)
#print("Enabled unicorn poop module!")
#time.sleep(.5)
#print("Pooping rainbows...")

i = 0.0
offset = 30
#while True:
stop = time.time()+10
while time.time() < stop:
        i = i + 0.3
        for y in range(height):
                for x in range(width):
                        r = 0
                        g = 0
                        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                        r = max(0, min(255, r + offset))
                        g = max(0, min(255, g + offset))
                        b = max(0, min(255, b + offset))
                        sense.set_pixel(x,y,int(r),int(g),int(b))
        time.sleep(0.01)
sense.clear()
