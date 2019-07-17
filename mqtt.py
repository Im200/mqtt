import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("gc/yourtopic")
    
#def on_message(client, userdata, msg):
    #print('\033[92' +msg.topic+":\033[0m\n "+str(msg.payload)+"\n")

client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message

client.connect("localhost", 1883, 60)

#client.loop_forever()
while True:
     message=input("Your message:")
     client.publish("topic",message)
