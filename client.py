import socket
import multiprocessing
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


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    p = multiprocessing.Process(target=receiving_msges, args=())
    p.start()

    while True:
        text = input(">>>")
        send(text)
        if text == DISCONNECT_MESSAGE:
            p.terminate()
            sys.exit()
