import socket

PORT = 5050
SERVER = "192.168.43.31"
ADDRESS = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)


def handle_client(conn, addr):
    print(f"New Connection {addr} Connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"Client : {msg}")
            if msg:
                conn.send("Message received".encode(FORMAT))

    conn.close()
    print("Connection Closed")


def start():
    s.listen()
    print(f"Listening to {SERVER}")
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)


print("Server is Starting")
start()
