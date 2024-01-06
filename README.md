# Jetson-X-Pi load balancing

First of all, I share the internet from my phone to both Jetson and Pi.
and I keep my phone very close to the Jetson so that it can act as a hotspot.

*The pi as a client then measures the link quality between it and the hotspot and using MQTT it publishes the info to the Jetson.
*The Jetson as the server subscribes to the MQTT topic.

.![Picture1](https://github.com/syrine-bouhoula/Jetson-X-Pi/assets/63754152/56a0f5a7-37e6-4e3f-8550-91f7784e230a)

* The jetson saves the info in a CSV file.
* In a real-time process the server checks if the link quality is low or high.

If the link quality is low then:
there will be a real-time object detection process on the pi.

![Picture2](https://github.com/syrine-bouhoula/Jetson-X-Pi/assets/63754152/8b24a9ed-c5c9-47e2-94d6-cedb834c7771)

If the link quality is high:
-The Pi will record a 30-second video and send it to the Jeston.
-The Jetson then does an object detection process on that video.

![Picture3](https://github.com/syrine-bouhoula/Jetson-X-Pi/assets/63754152/5a356d58-398b-43a9-94cd-3f66fd71534b)

