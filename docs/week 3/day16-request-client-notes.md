Today, I'll build a client-server application or automation for downloading firmware from an OTA server using Docker.

I'm building download_firmware.py and using my IPv4 because I also use Docker, and I'm creating an inbound rule for my IPv4 access. So, you'll need to know that the name for the inbound rule, or the name for running Docker, can be different because inbound rules and Docker must use TCP and port 8080 for local use. You'll need to set the inbound rule, the protocol for TCP, and the local port for 8080, and this also applies to Docker.

Set up an inbound rule in the terminal via administrator
New-NetFirewallRule `-DisplayName "Rule name"`
-Direction Inbound `-Protocol TCP`
-LocalPort "Port number" `
-Action "Action"

Then, here's how to set it up in Docker:
docker run: initial start to run
-d: run in the background
--name: container name
-p: port number

docker run -d --name 'port-name' -p 'local':'dockerhub' 'account-name'/'image-name':'version'

After that, we can access it like this:
docker start: to start the server
docker start 'container-name'

to monitor
docker ps: to view a list of running containers on the server
docker ps

and to stop them
docker stop: to shut down the server
docker stop 'container-name'

and to test to the OTA server client then we can use another device, for example I use my cellphone which already has pydroid3 with the flask and requests libraries after that then run download_firmware.py then you will find the results of the download automation and the file is saved depending on the coding content of download_firmware.py
