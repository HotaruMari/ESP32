from machine import Pin
from time import sleep_ms as slms
import network

def do_connect():
    
    wlan = network.WLAN(network.STA_IF) # create station interface
    wlan.active(True)   # activate the interface
    if not wlan.isconnected(): #if station interface conect with a new one
        print('connecting to network...')
        wlan.connect('Marisenal', 'Mariesgenial')  # connect to an AP
        while not wlan.isconnected(): #waiting conection
            pass
    print('network config:', wlan.ifconfig()) # get the interface's IP/netmask/gw/DNS addresses
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
print('Starting connection')
do_connect()
print('Connected')
print('Blink')
toggle(5)
print('OVER')