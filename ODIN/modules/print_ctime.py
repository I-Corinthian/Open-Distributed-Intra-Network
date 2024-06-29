import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from communication import com_utils as cu 

print_time = cu.init_clinet_soc()


try:
    while True:
        cu.subscribe(print_time,"time")
        print(f"current time is {cu.receive_data(print_time)}", end="\r")
except KeyboardInterrupt:
    cu.disconnect(print_time)