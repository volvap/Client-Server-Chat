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
<<<<<<< HEAD

def receiving_msges():
    while True:
        msg = client.recv(1024).decode(FORMAT)
        print(msg)
=======
    print(client.recv(1024).decode(FORMAT))

def receiving_msges():
    print(client.recv(1024).decode(FORMAT))
>>>>>>> 1da408d4981852a56cced85b671e5d44b4d1de3d

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
<<<<<<< HEAD
    thread = threading.Thread(target=receiving_msges, args=())
    thread.start()
=======
    #thread = threading.Thread(target=receiving_msges, args=())
    #thread.start()
>>>>>>> 1da408d4981852a56cced85b671e5d44b4d1de3d

    send("Hello World!")
    input()
    send("Hello Everyone!")
    input()
    send("Hello Vlad!")

    send(DISCONNECT_MESSAGE)
