import socket
import threading
import time


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNET_MESSAGE = "!DISCONNET"

client = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    if addr not in client:
        client.append(addr)

    connected = True

    while connected:
        data = conn.recv(1024)
        data_length = len(data)
        if data_length:
            msg = data.decode(FORMAT)
            if msg == DISCONNET_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == '__main__':
    print("[STARTING] server is starting....")
    start()
