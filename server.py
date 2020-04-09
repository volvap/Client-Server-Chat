import socket
import multiprocessing


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNET_MESSAGE = "!quit"


client = multiprocessing.Manager().dict()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        data = conn.recv(1024)
        data_length = len(data)
        if data_length:
            msg = data.decode(FORMAT)
            if msg == DISCONNET_MESSAGE:
                del client[addr]
                connected = False
            print(f"[{addr}] {msg}")
            broadcast(msg, addr)

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        client[addr] = conn
        p = multiprocessing.Process(target=handle_client, args=(conn, addr))
        p.start()
        print(f"[ACTIVE CONNECTIONS] {len(client)}")


def broadcast(msg, master_conn):
    for key, value in client.items():
        if master_conn == key:
            continue
        value.send(bytes(msg, "utf-8"))


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print("[STARTING] server is starting....")
    start()
