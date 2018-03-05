import pycom
import machine
import tiny_http
from network import WLAN

SSID = "SSID"
PASS = "PASS"

pycom.heartbeat(False)

wlan = WLAN(mode=WLAN.STA)
print("MAIN: WLAN Initialised")

nets = wlan.scan()
for net in nets:
    if net.ssid == SSID:
        wlan.connect(net.ssid, auth=(net.sec, PASS), timeout=5000)
        while not wlan.isconnected():
            machine.idle()
        print("Connected to network")

# Example tiny_http usage
# print(tiny_http.get_request("192.168.0.10", 5000, "/"))
