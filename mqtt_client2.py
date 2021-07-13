import paho.mqtt.client as mqtt
import threading
import time
import os

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8"))

def send_msg():
    while(1):
     msg = input()
     if(msg=="exit"):
         os._exit(1)

     client.publish("my/test/topic", client_id+"->"+msg)

def read_msg():
        client.loop_forever()
        

# create the client
client_id="Pc2"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("Username of HiveMQ here", "password here")

# connect to HiveMQ Cloud on port 8883
client.connect("HiveMQ cloud hostname here", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")
threading.Thread(target=read_msg).start()
threading.Thread(target=send_msg).start()


