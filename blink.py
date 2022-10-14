from machine import Pin
from time import sleep_ms as slms
import network

def toggle(max):
    lap=0
    while lap<max:

        led.value(1)
        slms(800)
        led.value(0)
        slms(800)
        lap += 1
led = Pin(2,Pin.OUT)

#MAIN-------------------------------------------------------
print('Blink')
toggle(5)
print('OVER')
