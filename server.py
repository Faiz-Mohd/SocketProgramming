import socket
import threading

PORT = 5050
SERVER = "192.168.43.31"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)


def handle_client(conn, addr):
    print(f"New Connection {addr} Connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            print("Disconnected")
        print(f"{addr}  {msg}")

    conn.close()
    print("Connection Closed")


def start():
    s.listen()
    print(f"Listening to {SERVER}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Conn {threading.activeCount() - 1}")


print("Server is Starting")
start()
