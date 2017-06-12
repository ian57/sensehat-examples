from sense_hat import SenseHat
import os
import time
import datetime

sense = SenseHat()

sense.set_rotation(180)
sense.clear()

inky=[]
for nbr in range(1, 15):
        inky.append(sense.load_image("sprites/inky"+str(nbr)+".png", redraw=False))
clyde=[]
for nbr in range(1, 15):
        clyde.append(sense.load_image("sprites/clyde"+str(nbr)+".png", redraw=False))

pinky=[]
for nbr in range(1, 15):
        pinky.append(sense.load_image("sprites/pinky"+str(nbr)+".png", redraw=False))

blinky=[]
for nbr in range(1, 15):
        blinky.append(sense.load_image("sprites/blinky"+str(nbr)+".png", redraw=False))

deadghost=[]
for nbr in range(1, 15):
        deadghost.append(sense.load_image("sprites/deadghost"+str(nbr)+".png", redraw=False))

pacman=[]
for nbr in range(1, 15):
        pacman.append(sense.load_image("sprites/pacman"+str(nbr)+".png", redraw=False))

def Move(sprites, direction):
        if direction:
                animation = sprites
        else:
                animation = reversed(sprites)
        for sprite in animation:
                sense.set_pixels(sprite)
                time.sleep(0.1) # delays for 100 miliseconds




print("Setting time")
bashCommand = "sudo service ntp stop; sudo ntpdate 193.50.119.254; sudo service ntp start"
os.system(bashCommand)
now = datetime.datetime.now()
print("Ok")
while (True):
	now = datetime.datetime.now()
	pressure = sense.get_pressure()
	temp = sense.get_temperature()
	humidity = sense.get_humidity() 
	Move(inky,0)
	sense.clear()
	sense.show_message(now.strftime("Date : %d %B %Y "), text_colour=[0, 255, 255])
	Move(blinky,0)
	sense.clear()
	sense.show_message(now.strftime("Heure : %H:%M"), text_colour=[255, 255, 0])
	Move(clyde,0)
	sense.clear()
	sense.show_message("Temperature : "+"{0:.1f}".format(temp)+" C", text_colour=[255, 255, 128])
	Move(pinky,0)
	sense.clear()
	sense.show_message("Pression : "+"{0:.0f}".format(pressure)+" mB", text_colour=[255, 0, 255])
	Move(pacman,0)
	sense.clear()
	sense.show_message("Hygrometrie : "+"{0:.0f}".format(humidity)+"%", text_colour=[255, 0, 255])
	Move(deadghost,0)
	sense.clear()
	Move(pacman,0)
	sense.clear()
	time.sleep(0.5)

