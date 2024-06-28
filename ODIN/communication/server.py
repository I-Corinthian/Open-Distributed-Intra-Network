import socket
import threading
import pickle
from communication import com_utils as cu
from communication import mainframecom as mfc

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(cu.ADDR)

def mainframe_calls(soc,addr):
    print(f"[NEW CONNECTION] {addr} connected to MainFrame")
    connected = True
    while connected:
        msg = cu.recive_calls(soc)
        if msg == cu.DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}") 
    soc.close()

def start():
    print("[STARTING] MainFrame is starting...")
    server.listen()
    try:
        while True:
            soc, addr = server.accept()
            thread = threading.Thread(target=mainframe_calls,args=(soc,addr))
            thread.start()
            print(f"[ACTIVE CONNECTION]{threading.active_count() - 1}") # cunected
    except KeyboardInterrupt:
        server.close()

