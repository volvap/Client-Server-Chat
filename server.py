import socket
import threading
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INIT, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    pass


def start():
    pass


print("[STARTING] server is starting....")
start()
