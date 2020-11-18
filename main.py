import ulogging as logging
import picoweb
from wifi import Wifi
import settings

# set up wifi class
wifi = Wifi(settings.wifi_ssid, settings.wifi_password)
# connect to wifi
wifi.connect()

app = picoweb.WebApp(__name__)


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")


app.run(debug=True, host="192.168.178.28")

