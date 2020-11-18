
import network


class Wifi:
    """A Wifi class that handles all the wifi functions
    
    :param ssid: SSID of the wifi
    :param wifi_password: password of the wifi
    
    """

    def __init__(self, ssid, wifi_password):
        self.wifi_ssid = ssid
        self.wifi_password = wifi_password

    def connect(self, hostname='flowerstation'):
        station = network.WLAN(network.STA_IF)

        if station.isconnected():
            print("Already connected")
            return

        station.active(True)
        station.config(dhcp_hostname=hostname)
        station.connect(self.wifi_ssid, self.wifi_password)

        while not station.isconnected():
            pass

        print("Connection successful")
        print(station.ifconfig())

