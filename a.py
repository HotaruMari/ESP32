from machine import Pin
from time import sleep_ms as slms

led = Pin(2,Pin.OUT)
def toggle(max):
    lap=0
    while lap<max:

        led.value(1)
        slms(800)
        led.value(0)
        slms(800)
        lap += 1
toggle(25)