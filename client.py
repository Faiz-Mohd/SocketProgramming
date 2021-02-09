import socket

PORT = 5050
SERVER = "192.168.43.31"
ADDRESS = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("Server :",client.recv(1024).decode(FORMAT))


send("Hello World")

