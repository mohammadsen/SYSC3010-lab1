# Mohammad Gaffori 101082318

from sense_emu import SenseHat 	
sense = SenseHat()

# Used for the Background 
lb = (173, 216, 230)
red = (255, 0, 0)
green = (0, 255,0)

while True:

    #Declaring & reading sensors
    temp = sense.get_temperature()
    press = sense.get_pressure()
    hum = sense.get_humidity()

    #rounding Value of sensors
    temp = round(temp,1)
    press = round(press,1)
    hum = round(hum,1)

    if temp< 7:
        bg = lb
    elif temp < 20: 
        bg = green
    else: 
        bg = red 

    message = "Temperature: " + str(temp) + " Pressure: " + str(press) + " Humidity: " + str(hum)


    sense.show_message(message, back_colour = bg, scroll_speed =0.05)
