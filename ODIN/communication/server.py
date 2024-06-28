import socket
import threading
import mainframecom as mfc

HEADER = 64
PORT = 3121
SERVER = socket.gethostname()
FORMAT = 'utf-8'
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "DISCONNECT!"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_clinet(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}") # got message
    conn.close()

def start():
    server.listen()
    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_clinet,args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}") # connected
    except KeyboardInterrupt:
        server.close()

print("[STARTING] MainFrame is starting...")
start()