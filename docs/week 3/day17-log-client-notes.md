in this day i will build logging for monitor activity client

My result if I use Flask Python to run IPv4 server is I successfully run download_firmware.py and get a log named developer_device.log. Next, if I use Flask Python to run IPv4 server is I successfully run download_firmware.py for PyDroid3 app from my phone. Next, if I use Docker to run OTA server is I successfully run download_firmware.py and get a log named docker_device.log, but in download_firmware.py I have to select localhost if it is successful. Lastly, if I use Docker to run OTA server for IPv4 is I successfully run download_firmware.py for PyDroid3 app from my phone.

The Docker-based OTA Server performed well. Test failures on the developer device were caused by accessing the host's own IPv4 address (10.136.176.226), while access via localhost was successful. This indicates a difference in the routing/loopback mechanism on Windows hosts compared to Docker port forwarding.

So if I use IPv4, then Flask will work for development and clients, and Docker for clients, but Docker for development only uses localhost.
