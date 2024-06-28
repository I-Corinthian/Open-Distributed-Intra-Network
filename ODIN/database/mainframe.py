import json
import os

temp_memory = os.path.join(os.path.dirname(__file__),"temp","memory.json")
topic = dict()


def add_topic(topic_name, data):
    if topic_name not in topic.keys():
        topic.update({topic_name:data})
        __update_memory()
        print("topic added")
    else:
        print("topic name already exists")

def terminate_topic(topic_name):
    try:
        topic.pop(topic_name)
        print("topic terminated")
    except KeyError:
        print("topic not found")
        
def update_topic(topic_name,data):
    try:
        topic.update({topic_name:data})
        __update_memory()
        print("topic updated")
    except KeyError:
        print("topic not found")

def read_topic(topic_name):
    return __read_memory(topic_name)


# Json helper
def __update_memory():
    with open(temp_memory,"w") as file:
        json.dump(topic,file)

def __read_memory(topic_name):
    with open(temp_memory,"r") as file:
        data = json.load(file)
        try:
            return data.get(topic_name)
        except KeyError:
            print("key missing")
            return None

def clean_memory():
    os.remove(temp_memory)

