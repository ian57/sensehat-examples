from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
sense.load_image("sprites/creeper.png",True)
time.sleep(1)
sense.clear()
time.sleep(1)
pixel_list = sense.load_image("sprites/creeper.png",False)
print("Wait!!!")
time.sleep(1)
print("Display!!!")
sense.set_pixels(pixel_list)
time.sleep(1)
sense.clear()

