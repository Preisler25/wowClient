import socket
from debug import debug


def connect():
    HOST = "127.0.0.1"
    PORT = 3000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

    debug("Received", repr(data))
    print(f"Received {data!r}")
