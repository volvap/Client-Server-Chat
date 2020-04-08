import socket
from multiprocessing import Process
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNET_MESSAGE = "!quit"

client = {}


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        data = conn.recv(1024)
        data_length = len(data)
        if data_length:
            msg = data.decode(FORMAT)
            if msg == DISCONNET_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            broadcast(msg, conn)

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        client[conn] = addr
        p = Process(target=handle_client, args=(conn, addr))
        p.start()
        print(f"[ACTIVE CONNECTIONS] {Process.activeCount() - 1}")


def broadcast(msg, master_conn):
    for sock in client:
        if sock == master_conn:
            continue
        sock.send(bytes(msg,"utf-8"))


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print("[STARTING] server is starting....")
    start()
