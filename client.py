import socket
import threading
import sys


PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!quit"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

def receiving_msges():
    while True:
        msg = client.recv(1024).decode(FORMAT)
        print(msg)
        if msg == DISCONNECT_MESSAGE:
            break

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    thread = threading.Thread(target=receiving_msges, args=())
    thread.start()

    while True:
        text = input("Input message: ")
        send(text)
        if text == DISCONNECT_MESSAGE:
            sys.exit()
