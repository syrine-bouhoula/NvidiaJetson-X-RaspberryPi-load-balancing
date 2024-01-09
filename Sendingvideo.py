import picamera
import requests
import time
import os

url = "http://192.168.0.35:8002/upload"  # replace with your Jetson Nano IP
print("On goign1")

camera = picamera.PiCamera()
print("On goign2")

camera.resolution = (640, 480)  # set the resolution
camera.framerate = 30  # set the framerate
print("On goign3")

while True:
    # create a unique filename for each video
    mp4_filename = "video_" + str(int(time.time())) + ".mp4"
    print("On goign")
    # start recording
    camera.start_recording(mp4_filename, format='h264')

    # wait for 30 seconds
    camera.wait_recording(30)

    # stop recording
    camera.stop_recording()

    # set the frame rate of the recorded video to 30 fps
    os.system("ffmpeg -i " + mp4_filename + " -r 30 -c:v copy temp.mp4")
    os.system("mv temp.mp4 " + mp4_filename)

    # send the video to Jetson Nano
    with open(mp4_filename, 'rb') as f:
        r = requests.post(url, files={'video': f})
        if r.status_code == 200:
            print("Video {} sent successfully!".format(mp4_filename))
         else:
            print("Failed to send video {}.".format(mp4_filename))

    # delete video file
    os.remove(mp4_filename)

