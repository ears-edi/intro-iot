import pycom
import machine
import time
import tiny_http
from network import WLAN

pycom.heartbeat(False)

SSID = "created-iot-workshop"
PASS = "created2018"
IP = "10.0.0.254"
PORT = 5000
ENDPOINT = "/putldrdata/"
CHANNEL = 1

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
x = tiny_http.TinySocket(IP, PORT)
x.connect()
x.send_request("/")
print(x.get_response())
x.close()

adc = machine.ADC()
read_pin = adc.channel(pin="P16")

while True:
  x.connect()
  x.send_request(ENDPOINT + str(CHANNEL) + "/" + str(read_pin()))
  print(x.get_response())
  x.close()
  time.sleep(1)
