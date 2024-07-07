import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from communication import com_utils as cu 

cal = cu.init_clinet_soc()

def print_overwrite(message):
    sys.stdout.write('\033[2K\033[1G')
    sys.stdout.write('\r' + message)
    sys.stdout.flush()

def calculate(num1,num2,operation):
    if num1 is None or num2 is None:
        print("WAITING")
        return
    result = None
    if operation == "+":
        result = num1 + num2
        print_overwrite(f"[ANSWER]: {result}")
    elif operation == "-":
        result = num1 - num2
        print_overwrite(f"[ANSWER]: {result}")
    elif operation == "*":
        result = num1 * num2
        print_overwrite(f"[ANSWER]: {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print_overwrite(f"[ANSWER]: {result}")
        else:
            result = "undefined (division by zero)"

    

while True:
    try:
        is_available = cu.topics_available(cal)
        data = cu.receive_data(cal)
        while "neural_op" in data:
            cu.subscribe(cal,"neural_op")
            data = cu.receive_data(cal)
            calculate(data[0],data[1],data[2])
    except KeyboardInterrupt:
        cu.disconnect(cal)
