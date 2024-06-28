import socket
import com_utils as cu

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send(msg):
    message = msg.encode(cu.FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(cu.FORMAT)
    send_length += b' ' * (cu.HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def disconnected():
    send(cu.DISCONNECT_MESSAGE)

client.connect(cu.ADDR)
cu.send(client,"hello world")
disconnected()