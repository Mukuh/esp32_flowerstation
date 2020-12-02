import ulogging as logging
import picoweb
from wifi import Wifi
import settings

# set up wifi class
wifi = Wifi()
if settings.wifi_ssid is not None and settings.wifi_password is not None:
    # connect to wifi
    wifi_status = wifi.connect(settings.wifi_ssid, settings.wifi_password)
else:
    wifi_status = wifi.open_access_point(access_point_name=settings.access_point_name,
                                         access_point_password=settings.access_point_password)

print("[INFO] wifi status %s" % wifi_status)

app = picoweb.WebApp(__name__)


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")


app.run(debug=True, host="192.168.178.28")
