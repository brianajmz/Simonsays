import RPi.GPIO as GPIO
import LEDRGB as LED  
import time
import random
colors = ['R', 'G', 'B', 'Y']
# breadboard setup 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# this script bliks one of four random colors on the RGB LED
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)


# this script appends a value to a list 
def append_list():
    while True:
        for i in range(0, len(colors)):
            n = random.randint(0,3)
            colors.append(colors[n])
            color_string = ' '.join(colors)
            LED.setColor(colors[n])
            time.sleep(0.5)
            LED.noColor()
            time.sleep(0.5)

if __name__ == '__main__':
    try:
        append_list()
        LED.destroy()
    except KeyboardInterrupt:
        print 'Good Bye'
