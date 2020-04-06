import socket
import threading


PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
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
    thread = threading.Thread(target=receiving_msges, args=())
    thread.start()

    send("Hello World!")
    input()
    send("Hello Everyone!")
    input()
    send("Hello Vlad!")

    send(DISCONNECT_MESSAGE)
