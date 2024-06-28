from database import mainframe as mf

def publish(topic_name,data):
    if topic_name in mf.topic.keys():
        mf.update_topic(topic_name,data)
    else:
        mf.add_topic(topic_name,data)

def subscrib(topic_name):
    return mf.read_topic(topic_name)