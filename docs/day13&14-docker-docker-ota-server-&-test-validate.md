Today I'm going to build an OTA server using Docker.

First, I downloaded Docker Desktop, then in Docker Local I created a Dockerfile and .dockerignore to set up my OTA server.

Next, I'll create a requirements.txt to use the Dockerfile, as the Dockerfile will install all the Python requirements from requirements.txt. Simply run pip and navigate to requirements.txt.

Next, I'll create an OTA server script in server.py. If I use the URL path to /signature.sig, this file will be downloaded, and if I use the URL path /firmware.bin, this file will also be downloaded.

Finally, when I run GitHub actions, for each sign_firmware run, we'll create a Docker image and then register the image on DockerHub.
