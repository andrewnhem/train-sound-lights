import os, time, sys
from gpiozero import LED, Button
from signal import pause
import simpleaudio as sa

led1 = LED(17)
led2 = LED(18)
led3 = LED(27)
button1 = Button(2)
button2 = Button(3)
button3 = Button(4)
wave_obj = sa.WaveObject.from_wave_file('test.wav')
play_obj = wave_obj.play()

button1.when_pressed = led1.toggle
button2.when_pressed = led2.toggle
button3.when_pressed = play_obj

pause()