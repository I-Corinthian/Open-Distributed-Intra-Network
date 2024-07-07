import socket
import threading
from communication import com_utils as cu
from communication import mainframecom as mfc

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(cu.ADDR)

def mainframe_calls(soc,addr):
    print(f"[NEW CONNECTION] {addr} connected to MainFrame")
    connected = True
    while connected:
        msg = cu.receive_data(soc)
        if msg:
            if msg == cu.DISCONNECT_MESSAGE:
                connected = False
                break
            if msg[0] == "publisher":
                mfc.publish(msg[1],msg[2])
            elif msg[0] == "subscriber":
                respose = mfc.subscribe(msg[1])
                cu.send_data(soc,respose)
            elif msg == "get_avilable_topics":
                respose = mfc.get_avilable_topics()
                cu.send_data(soc,respose)
            else:
                print(f"[{addr}] {msg}")
    soc.close()

def start():
    print("[STARTING] MainFrame is starting...")
    server.listen()
    mfc.init_mainframe()
    try:
        while True:
            soc, addr = server.accept()
            thread = threading.Thread(target=mainframe_calls,args=(soc,addr))
            thread.start()
            print(f"[ACTIVE CONNECTION]{threading.active_count() - 1}") 
    except KeyboardInterrupt:
        mfc.clean_mainframe()
        server.close()