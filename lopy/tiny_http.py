import socket

def parse_return_data(data_b):
    newline_count = 0
    start = 0
    # goes through data_b until it finds 2 consecutive newline characters
    for idx, c in enumerate(data_b):
        if newline_count == 2:
            start = idx
            break
        if chr(c) == "\n":
            newline_count += 1
        elif chr(c) != "\r":
            newline_count = 0
    return data_b[start:]

class TinySocket():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.sock.settimeout(5) # seconds

        try:
            #s.connect(socket.getaddrinfo(host, port)[0][-1])
            self.sock.connect((self.host, self.port))
        except OSError:
            print("Caught OSError trying to connect to server, are you sure the server is up?")

    def send_request(self, endpoint):
        """ Sends a GET request to host:port/endpoint and returns the body
            of the response. Please note, endpoint should begin with a slash "/"
        """
        data = bytes("GET {} HTTP/1.1\nHost: {}:{}\n\n".format
                        (endpoint, self.host, self.port), "utf-8")

        self.sock.send(data)

    def get_response(self):
        total = b""
        data = None

        while data != b"":
            data = self.sock.recv(128)
            total += data

        return parse_return_data(total)

    def close(self):
        self.sock.close()
