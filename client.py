import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISSCONNET_MESSAGE = "!DISCONNET"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
