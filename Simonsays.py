import RPi.GPIO as GPIO
import LEDRGB as LED  
import time
import random
from getpass import getpass
colors = ['R', 'G', 'B', 'Y']
# breadboard setup 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# this script bliks one of four random colors on the RGB LED
colors = ['R', 'G', 'B', 'Y']
frequencies = [200, 300, 400, 500]
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

buzz_pin = 32
GPIO.setup(buzz_pin,GPIO.OUT)   
Buzz = GPIO.PWM(buzz_pin,1000)
color_sequence = []
frequency_sequence = []

def validate_guess(color_sequence_string,guess):
    if color_sequence_string == guess:
        print "Correct"
    else : #if the user doesn't guess correctly, then print 'You Lose'
        print "You Lose :("
        exit()
# this script appends a value to a list 
def append_list():
    while True:
        n = random.randint(0,3)
        color_sequence.append(colors[n])
        frequency_sequence.append(frequencies[n])
        for i in range(0, len(color_sequence)):
            Buzz.ChangeFrequency(frequency_sequence[i])
            Buzz.start(50)
            LED.setColor(color_sequence[i]) 
            time.sleep(0.5)
            Buzz.stop()
            LED.noColor()
            time.sleep(0.5)
        guess = getpass("Guess the color sequence")  
        color_sequence_string=''.join(color_sequence)
        validate_guess(color_sequence_string,guess.upper())
    

if __name__ == '__main__':
    try:
        print "Type in the color sequence, R = red, G = green, B = blue, Y= yellow"
        append_list()
        LED.destroy()
    except KeyboardInterrupt:
        print 'Good Bye'
