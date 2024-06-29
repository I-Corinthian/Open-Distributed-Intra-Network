import com_utils as cu

client = cu.init_clinet_soc()


try:
    while True:
        cu.subscribe(client,"time")
        print(cu.receive_data(client))
except KeyboardInterrupt:
    cu.disconnect(client)