import signal
import time
from sys import exit
from sense_hat import SenseHat

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

def readSprites(filename):
	img = Image.open(filename)
	sprites_list = []
	for o_x in range(int(img.size[0]/8)):
	    for o_y in range(int(img.size[1]/8)):
	        sprite=[]
	        for x in range(8):
        	    for y in range(8):
                	pixel = img.getpixel(((o_x*8)+y,(o_y*8)+x))
        	        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                	sprite.append([r,g,b])
	        sprites_list.append(sprite)
	return sprites_list

def animateSprite(sprite,delay=0.1):
	for index,spr in enumerate(sprite):
	        sense.clear()
        	sense.set_pixels(spr)
	        time.sleep(delay)

sense = SenseHat()

sense.set_rotation(180)

#img = Image.open('sprites/skullsHflip.png')
#sprites_list = []
#for o_x in range(int(img.size[0]/8)):
#    for o_y in range(int(img.size[1]/8)):
#	sprite=[]
#
#       for x in range(8):
#          for y in range(8):
#             pixel = img.getpixel(((o_x*8)+y,(o_y*8)+x))
#               r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
#		sprite.append([r,g,b])
#	sprites_list.append(sprite)

sprite1 = readSprites('sprites/skulls.png')
sprite2 = readSprites('sprites/orange1-sheet.png')
sprite3 = readSprites('sprites/pacman_movb-sheet.png')

animateSprite(sprite1)
animateSprite(sprite2,0.05)


for index,spr in enumerate(sprite3):
	sense.clear()
	sense.set_pixels(spr)
	time.sleep(0.1)
sense.clear()
