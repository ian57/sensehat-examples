#!/usr/bin/env python

from time import sleep
from sys import exit

try:
    from pyfiglet import figlet_format
except ImportError:
    exit("This script requires the pyfiglet module\nInstall with: sudo pip install pyfiglet")

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.set_rotation(90)

width = 8
height = 8

TXT = "Hackable is fun!!!"

figletText = figlet_format(TXT+' ', "3-d", width=1000) # banner font generates text with heigth 7
print(figletText)
textMatrix = figletText.split("\n")[:width] # width should be 8 on both HAT and pHAT!
textHeight = len(textMatrix)
if textMatrix[textHeight-1]=='':
	textHeight = textHeight -1
textWidth = len(textMatrix[0]) # the total length of the result from figlet
i = -1

def step():
    global i
    if i>=100*textWidth :
	i = 0 
    else: 
	i=i+1
#    i = 0 if i>=100*textWidth else i+1 # avoid overflow
    for h in range(height):
        for w in range(textHeight):
            hPos = (i+h) % textWidth
            chr = textMatrix[w][hPos]
	    if chr in ['/', '\\', '_', '(',')','d','8','P', 'b', 'Y', '8','o', '^', '|', '-', '`', 'a', '"' ]:
                sense.set_pixel(width-w-1, h, 255, 255, 255)
            elif chr == '#':
                sense.set_pixel(width-w-1, h, 255, 0, 0)
            elif chr == '*':
                sense.set_pixel(width-w-1, h, 255, 0, 0)
            elif chr == ':':
		sense.set_pixel(width-w-1, h, 255, 255, 255)
            elif chr == '.':
		sense.set_pixel(width-w-1, h, 128, 255, 128)
            elif chr == '+':
		sense.set_pixel(width-w-1, h, 255, 0, 255)
            elif chr == '@':
		sense.set_pixel(width-w-1, h, 255, 0, 0 )
            elif chr == '!':
		sense.set_pixel(width-w-1, h, 255, 128, 128)
            elif chr == '\'':
		sense.set_pixel(width-w-1, h, 255, 0, 128)
	    else:
                sense.set_pixel(width-w-1, h, 0, 0, 0)

sense.clear()

#while True:
for i in range (0, 1*textWidth-8):
    step()
    sleep(0.04)

sense.clear()
