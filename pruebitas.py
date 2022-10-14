import urequests as requests
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
# Define the remote file to retrieve
remote_url = 'https://www.google.com/robots.txt'

# Define the local filename to save data
local_file = 'local_copy.txt'
# Make http request for remote file data
data = requests.get(remote_url)
# Save file data to local copy
with open(local_file, 'wb')as file:
    file.write(data.content)