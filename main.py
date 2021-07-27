import ulogging as logging
import picoweb
from wifi import Wifi
import settings
import upip
import os

fs_stat = os.statvfs('/')
fs_size = fs_stat[0] * fs_stat[2]
fs_free = fs_stat[0] * fs_stat[3]
print("* [INFO] File System Size {:,} - Free Space {:,}".format(fs_size, fs_free))

# set up wifi class
wifi = Wifi()

# scan for wifi networks
networks = wifi.scan_wifi()

if settings.wifi_ssid is not None and settings.wifi_password is not None:
    # connect to wifi
    wifi_status = wifi.connect(settings.wifi_ssid, settings.wifi_password)
else:
    wifi_status = wifi.open_access_point(access_point_name=settings.access_point_name,
                                         access_point_password=settings.access_point_password)

print("* [INFO] wifi status %s" % wifi_status)

app = picoweb.WebApp(__name__)

try:
    f = open("templates/welcome_html.py", "r")
    f.close()
    print("* [INFO] found templates/welcome_html.py")
    print("* [INFO] deleting templates/welcome_html.py")
    os.remove("templates/welcome_html.py")
except OSError:
    pass

try:
    f = open("templates/scan_html.py", "r")
    f.close()
    print("* [INFO] found templates/scan_html.py")
    print("* [INFO] deleting templates/scan_html.py")
    os.remove("templates/scan_html.py")
except OSError:
    pass


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "welcome.html", (req, ))


@app.route("/scan")
def scan(req, resp):
    yield from picoweb.start_response(resp)
    # it is only possible to call the render_template function with one argument?
    yield from app.render_template(resp, "scan.html", (networks, ))


app.run(debug=True, host="192.168.178.28")
