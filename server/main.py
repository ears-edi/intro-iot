import time
import json
from flask import Flask, render_template, send_from_directory

num_channels = 20

app = Flask(__name__)
ldr_data = [[] for i in range(num_channels)]

@app.route('/')
def hello_world():
    """ You can use this to test that get_request is working.
        If get_request returns "hello" on "/" then it works.
    """
    return "hello"

@app.route('/putldrdata/<int:channel>/<int:data>')
def put_ldr_data(channel, data):
    """ Stores the LDR value with the current time """
    ldr_data[channel].append((time.time(), data))
    return "OK, channel: " + str(channel) + " data: " + str(data)

@app.route('/getldrdata/<int:channel>')
def get_ldr_data(channel):
    """ Returns all LDR data as a string """
	if channel >= 0 and channel < num_channels:
		return str(ldr_data[channel])
		
	else:
		return "channel " + str(channel) + " out of range"
		
@app.route('/logger')
def logger():
	""" Returns html file for logger char """
	return render_template('logger.html')
	
@app.route('/logger/<path:path>')
def send_js(path):
	return send_from_directory('templates', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
