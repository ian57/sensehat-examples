#!/usr/bin/env python

from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

height = 8
width = 8

ASCIIPIC=[
     "  XXXX  "
    ," X    X "
    ,"X X  X X"
    ,"X      X"
    ,"X X  X X"
    ,"X  XX  X"
    ," X    X "
    ,"  XXXX  "	
    ]

ASCIIPIC=[
     "  XXXX  "
    ," XXXXXX "
    ,"XX-XX-XX"
    ,"XXXXXXXX"
    ,"XXXXXXXX"
    ,"XX-XX-XX"
    ," XX--XX "
    ,"  XXXX  "	
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ,"        "
    ]
i = -1

def step():
    global i
    i = 0 if i>=100*len(ASCIIPIC) else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % len(ASCIIPIC)
            chr = ASCIIPIC[hPos][w]
            if chr == ' ':
                sense.set_pixel(w, h, 0, 0, 0)
	    elif chr == '-':
                sense.set_pixel(w, h, 255, 255, 255)
            else:
                sense.set_pixel(w, h, 255, 255, 0)

while True:
    step()
    sleep(0.2)
