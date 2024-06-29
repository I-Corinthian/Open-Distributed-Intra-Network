import com_utils as cu

client = cu.init_clinet_soc()
cu.publish(client,"time",1)
cu.disconnect(client)