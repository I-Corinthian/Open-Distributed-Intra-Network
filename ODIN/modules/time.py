import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from communication import com_utils as cu 
import time

time_pub = cu.init_clinet_soc()

try:
    i = 0
    print("[TIMER STARTED]")
    while True:
        cu.publish(time_pub,"time",i)
        i += 1
        time.sleep(1.0)
except KeyboardInterrupt:
    cu.disconnect(time_pub)