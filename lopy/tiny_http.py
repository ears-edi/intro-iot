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

def get_request(host, port, endpoint):
    """ Sends a GET request to host:port/endpoint and returns the body
        of the response. Please note, endpoint should begin with a slash "/"
    """
    # create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.settimeout(5) # seconds
    try:
        s.connect(socket.getaddrinfo(host, port)[0][-1])
    except OSError:
        print("Caught OSError trying to connect to server, are you sure the server is up?")
    print("Connected to server")
    s.send(bytes(
            "GET {} HTTP/1.1\nHost: {}:{}\n\n".format(endpoint,
                                                      host,
                                                      port),
            "utf-8"))
    total = b""
    data = None
    while data != b"":
        data = s.recv(100)
        total += data
    return parse_return_data(total)
