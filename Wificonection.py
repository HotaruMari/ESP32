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
print('Starting connection')
do_connect()
print('Connected')

