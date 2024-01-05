import paho.mqtt.client as mqtt
import subprocess
import re
import time

# Define MQTT broker details
broker_address = "broker.emqx.io"
broker_port = 1883
topic = "link_quality01"

# Define function to get link quality
def get_link_quality():
    while True:
        p = subprocess.Popen(['iwconfig', 'wlan0'], stdout=subprocess.PIPE)
        output = p.communicate()[0]
        quality_match = re.search('Link Quality=(\d+)/(\d+)', output.decode('utf-8'))
        if quality_match:
            link_quality = int(quality_match.group(1)) / int(quality_match.group(2))
            print("Link quality: {:.2f}".format(link_quality))
            client.publish(topic, link_quality)
        time.sleep(1)

# Define MQTT client and callbacks
client = mqtt.Client()
client.connect(broker_address, broker_port, 60)

# Run the link quality function and publish the results to the MQTT broker
get_link_quality()


