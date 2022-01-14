from sense_emu import SenseHat 

sense = SenseHat()

pink = (255, 192, 203)
red = (255, 0, 0)

while True:
    sense.show_message("Mohammad Gaffori", text_colour=red, back_colour=pink, scroll_speed =0.25)
    #sense.show_message("mohammad Gaffori")