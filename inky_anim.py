from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()

sense.set_rotation(180)

inky=[]
for nbr in range(1, 15):
	inky.append(sense.load_image("sprites/inky"+str(nbr)+".png", redraw=False))

def Move(sprites, direction):
        if direction:
		animation = sprites
        else:
		animation = reversed(sprites)
        for sprite in animation:
                sense.set_pixels(sprite)
                time.sleep(0.1) # delays for 100 miliseconds

Move(inky,1)
sense.clear()  # no arguments defaults to off
time.sleep(1)
Move(inky,0)
sense.clear()  # no arguments defaults to off
time.sleep(1)

