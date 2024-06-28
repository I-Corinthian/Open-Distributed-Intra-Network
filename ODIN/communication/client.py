import socket

HEADER = 64
PORT = 3121
SERVER = socket.gethostname()
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def disconnect():
    send(DISCONNECT_MESSAGE)

client.connect(ADDR)
send("hello world")
disconnect()