from sense_hat import SenseHat
import os
import time
import datetime

sense = SenseHat()

sense.set_rotation(180)
sense.clear()

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
	sense.show_message(now.strftime("Date : %d %B %Y "), text_colour=[0, 255, 255])
	sense.show_message(now.strftime("Heure : %H:%M"), text_colour=[255, 255, 0])
	sense.show_message("Temperature : "+"{0:.1f}".format(temp)+" C", text_colour=[255, 255, 128])
	sense.show_message("Pression : "+"{0:.0f}".format(pressure)+" mB", text_colour=[255, 0, 255])
	sense.show_message("Hygrometrie : "+"{0:.0f}".format(humidity)+"%", text_colour=[255, 0, 255])


