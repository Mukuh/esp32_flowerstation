
import network
import utime as time


class Wifi:
    """A Wifi class that handles all the wifi functions
    
    """

    def __init__(self):
        self.wifi_ssid = None
        self.wifi_password = None
        self.access_point_name = None
        self.access_point_password = None

    def connect(self, ssid, wifi_password, hostname='flowerstation'):
        """Connect to a wifi

        :param ssid: wifi service set identifier (wifi name)
        :param wifi_password: wifi password
        :param hostname: optional dhcp hostname
        :return: interface status
        """
        self.wifi_ssid = ssid
        self.wifi_password = wifi_password

        station_interface = network.WLAN(network.STA_IF)

        if station_interface.isconnected():
            print("* [INFO] WIFI Already connected")
            return station_interface.status()

        station_interface.active(True)
        station_interface.config(dhcp_hostname=hostname)

        # try three times to connect to the wifi
        for _ in range(3):
            station_interface.connect(self.wifi_ssid, self.wifi_password)

            for _ in range(15):
                if station_interface.isconnected():
                    print("* [INFO] WIFI Connection successful")
                    print("* [INFO] WIFI IP: %s" % station_interface.ifconfig()[0])
                    return station_interface.status()
                time.sleep_ms(200)

        print("* [ERROR] Failed to connect to wifi %s" % self.wifi_ssid)
        return station_interface.status()

    @staticmethod
    def scan_wifi():
        """Scan the network for available wifis

        :return: a list of tuples (ssid, bssid, channel, RSSI, authmode, hidden)
        """
        station_interface = network.WLAN(network.STA_IF)

        station_interface.active(True)
        networks = station_interface.scan()
        station_interface.active(False)
        return networks

    def open_access_point(self, access_point_name, access_point_password):
        """Open an access point

        :param access_point_name: access point service set identifier (AP name)
        :param access_point_password: access point password
        :return: interface config as tuple [IP address, subnet mask, gateway and DNS server]
        """
        self.access_point_name = access_point_name
        self.access_point_password = access_point_password

        ap_interface = network.WLAN(network.AP_IF)

        ap_interface.active(True)
        ap_interface.config(essid=self.access_point_name, password=self.access_point_password)

        while ap_interface.active() is False:
            pass

        print("* [INFO] Access-Point ready")
        print(ap_interface.ifconfig())

        return ap_interface.status()

