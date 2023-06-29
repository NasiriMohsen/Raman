import network

sta_if = network.WLAN(network.STA_IF)

#sta_if.active(True)
#sta_if.connect('Wifi','Pass')

if not sta_if.isconnected():
    print('Connecting to Wifi...')
    sta_if.active(True)
    sta_if.connect('Wifi','Pass')
    while not sta_if.isconnected():
        pass
print('Network config: ', sta_if.ifconfig())