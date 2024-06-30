import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from communication import com_utils as cu 

front_end = cu.init_clinet_soc()


window = Tk() 
topics = list()

window.geometry("920x480")
window.title("ODIN GUI")

def get_topics():
    cu.send_data(front_end,"get_avilable_topics")
    avilable_topics = cu.receive_data(front_end)
    topics = avilable_topics
    for count, ele in enumerate(topics):
        list.insert(count,ele)


    
title = Label(window,text="TOPICS",font=("Arial",12,'bold'))
get = Button(window,text="GET TOPICS",command=get_topics,font=("Arial",6),height=1,width=15)
list = Listbox(window)

try:
    title.place(x=30,y=20)
    get.place(x=150,y=20)
    list.place(x=40,y=60)
    window.mainloop()
except KeyboardInterrupt:
    cu.disconnect(front_end)

