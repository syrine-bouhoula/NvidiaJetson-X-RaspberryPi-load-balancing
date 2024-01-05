import subprocess
import paho.mqtt.client as mqtt

# Set up MQTT client
client = mqtt.Client()
client.username_pw_set(username="", password="")
client.connect("broker.emqx.io")

# Define function to execute object detection script
def run_object_detection_script():
    print("Running object detection script...")
    subprocess.run(["python3", "real_time_object_detection.py", "--prototxt", "MobileNetSSD_deploy.prototxt.txt", "--model", "MobileNetSSD_deploy.caffemodel">


# Define callback function for incoming messages
def on_message(client, userdata, message):
    print("Received message on topic:", message.topic)
    print("Message payload:", message.payload.decode())
    msg= message.payload.decode()
    print(msg)
    if message.topic == "link_quality" and msg == "low":
        print("Received a 'low' link quality message")
        run_object_detection_script()

# Subscribe to incoming messages
client.subscribe("link_quality")
client.on_message = on_message
client.loop_forever()


