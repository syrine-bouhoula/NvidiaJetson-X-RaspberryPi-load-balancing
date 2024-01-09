
import paho.mqtt.client as mqtt
import csv

# Define MQTT broker details
broker_address = "broker.emqx.io"
broker_port = 1883
topic = "link_quality01"

# Define function to save data to CSV file
def save_to_csv(data):
    with open('link_quality.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data])

# Define MQTT client and callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    save_to_csv(float(msg.payload.decode()))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()
