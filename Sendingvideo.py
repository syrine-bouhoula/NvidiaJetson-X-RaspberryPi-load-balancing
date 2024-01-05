import picamera
import requests
import time
import os
import paho.mqtt.client as mqtt

# Set up MQTT client
client = mqtt.Client()
client.username_pw_set(username="", password="")
client.connect("broker.emqx.io")

# Set up camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)  # set the resolution
camera.framerate = 30  # set the framerate

# Set up URL for Jetson Nano
url = "http://192.168.0.35:8000/upload"  # replace with your Jetson Nano IP

# Define link quality threshold
link_quality_threshold = 0.7

def on_message(client, userdata, message):
    # Get the payload value from the message
    payload = message.payload.decode()

    # Check if the payload is "high" and start recording and sending the video
    if payload == "high":
        # create a unique filename for each video
        mp4_filename = "video_" + str(int(time.time())) + ".h264"

        # start recording
        camera.start_recording(mp4_filename, format='h264')

        # wait for 30 seconds
        camera.wait_recording(30)

        # stop recording
 # convert the video to mp4 format
        mp4_filename_converted = mp4_filename.replace(".h264", ".mp4")
        os.system("MP4Box -add " + mp4_filename + " " + mp4_filename_converted)

        # send the video to Jetson Nano
        with open(mp4_filename_converted, 'rb') as f:
            r = requests.post(url, files={'video': f})
            if r.status_code == 200:
                print("Video {} sent successfully!".format(mp4_filename_converted))
            else:
                print("Failed to send video {}.".format(mp4_filename_converted))

        # delete video files
        os.remove(mp4_filename)
        os.remove(mp4_filename_converted)

    # If the payload is "low", print a log message
    elif payload == "low":
        print("Link quality is low. Not recording or sending video.")

client.subscribe("link_quality")
client.on_message = on_message

while True:
    client.loop()
    time.sleep(0.1)  # Add a small delay to allow the program to print the messages
