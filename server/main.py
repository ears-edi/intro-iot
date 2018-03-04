import time
from flask import Flask

app = Flask(__name__)
ldr_data = []

@app.route('/')
def hello_world():
    """ You can use this to test that get_request is working.
        If get_request returns "hello" on "/" then it works.
    """
    return "hello"

@app.route('/putldrdata/<int:data>')
def put_ldr_data(data):
    """ Stores the LDR value with the current time """
    ldr_data.append((time.time(), data))
    return "OK"

@app.route('/getldrdata')
def get_ldr_data():
    """ Returns all LDR data as a string """
    return str(ldr_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
