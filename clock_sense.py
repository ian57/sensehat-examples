#!/usr/bin/env python

import signal
import threading
import time

from graphics import Drawing, Color
from sense_hat import SenseHat

sense = SenseHat()

print("""Clock

Displays an analog clock.

Automatically dims at night.
""")

class SenseHatDrawing(Drawing):
  def __init__(self):
    Drawing.__init__(self,8,8)

  '''
  All drawing operations use the pixel method
  so we override it for UnicornHat
  '''
  def pixel(self, x, y, col):
    if x < 0 or x > 7 or y < 0 or y > 7:
      return False
    self.buffer[(x,y)] = col
    sense.set_pixel(x, y, col.r, col.g, col.b)

#  def show(self):
#    unicorn.show()

d = SenseHatDrawing()

# X offset of clock centre
O_X = 3
# Y offset of clock centre
O_Y = 3
# Radius of clock
R = 3
# Rotation offset of clock, set to 0, 90, 180, 270, etc
sense.set_rotation(0)

def setBrightness(currenttime):
  currenthour = currenttime.tm_hour
  # if it's between 10 am and 8 pm,
  # use dimmer brightness
  if(currenthour < 10 or currenthour > 20):
    sense.low_light = True
  else:
    sense.low_light = False

def tick():
  currenttime = time.localtime()
  currenthour = currenttime.tm_hour
  currentmin  = currenttime.tm_min
  currentsec  = currenttime.tm_sec

  # Set daytime or nighttime brightness
  setBrightness(currenttime)

  d.clear()
  # Draw the circle around the clock
  d.circle(O_X,O_Y,R,Color(255,255,255))

  # Draw the clock hands
  d.circle_line(O_X,O_Y,R-1,(-360.0*((currenthour % 12)/12.0)),Color(255,0,0))
  d.circle_line(O_X,O_Y,R-1,(-360.0*(currentmin/60.0)), Color(0,255,0))
  d.circle_line(O_X,O_Y,R-1,(-360.0*(currentsec/60.0)), Color(0,0,255))

  # draw buffer to hardware
  #d.show()

  threading.Timer(1,tick).start()

tick()
