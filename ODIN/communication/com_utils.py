import socket
import pickle
HEADER = 1024
PORT = 3121
SERVER = socket.gethostname()
FORMAT = 'utf-8'
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "DISCONNECT!"


def receive_data(soc):
    msg_length = soc.recv(HEADER).decode(FORMAT)
    receiving = True
    try:
        while receiving:
            if msg_length:
                msg_length = int(msg_length)
                full_msg = b""
                while len(full_msg) < msg_length:
                    part = soc.recv(msg_length - len(full_msg))
                    full_msg += part
                return pickle.loads(full_msg)
    except (BrokenPipeError,ConnectionResetError) as e:
        if soc:
            soc.close() 
    return None

def send_data(soc,msg):
    try:
        message = pickle.dumps(msg)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        soc.send(send_length)
        soc.send(message)
    except (BrokenPipeError,ConnectionResetError) as e:
        if soc:
            soc.close() 

def publish(soc,topic_name,data):
    send_data(soc,("publisher",topic_name,data))

def subscribe(soc,topic_name):
    return send_data(soc,("subscriber",topic_name))

def disconnect(soc):
    send_data(soc,DISCONNECT_MESSAGE)

def topics_available(soc):
    return send_data(soc,("get_avilable_topics"))

def init_clinet_soc():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    return client