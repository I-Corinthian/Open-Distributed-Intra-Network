import socket
HEADER = 64
PORT = 3121
SERVER = socket.gethostname()
FORMAT = 'utf-8'
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "DISCONNECT!"


def recive_calls(soc):
    msg_length = soc.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = soc.recv(msg_length).decode(FORMAT)
        return msg

def send(soc,msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    soc.send(send_length)
    soc.send(message)