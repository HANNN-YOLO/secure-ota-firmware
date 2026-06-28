# Docker Deployment Guide (IPv4 Network)

This guide explains how to deploy an application using Docker with an IPv4 network approach. It also covers firewall configuration, Docker image management, Docker Hub publishing, and container execution.

---

# Prerequisites

Before starting, make sure you have:

- Docker Desktop installed
- Docker Hub account
- Administrator access (Windows)
- Internet connection

---

# Step 1 - Create a Windows Firewall Rule

Open **Windows PowerShell** as **Administrator**, then create an inbound rule.

```powershell
New-NetFirewallRule `
-DisplayName "Rule name" `
-Direction Inbound `
-Protocol TCP `
-LocalPort "Port number" `
-Action Allow
```

Example:

```powershell
New-NetFirewallRule `
-DisplayName "Docker API" `
-Direction Inbound `
-Protocol TCP `
-LocalPort 8000 `
-Action Allow
```

This allows incoming TCP traffic on the specified port.

---

# Step 2 - Login to Docker Hub

Login using your Docker Hub account.

```bash
docker login
```

Enter:

- Docker Hub Username
- Docker Hub Password

---

# Step 3 - Create a Docker Image

First, create a `Dockerfile`.

Example project structure:

```
project/
│
├── Dockerfile
├── app.py
└── requirements.txt
```

Then build the image.

```bash
docker build -t image-name .
```

Example

```bash
docker build -t secure-ota-server .
```

The `-t` option assigns a name to the image.

---

# Step 4 - Tag the Docker Image

Docker tags work similarly to software versioning.

```bash
docker tag image-name image-name:version
```

Example

```bash
docker tag secure-ota-server secure-ota-server:v1.0.0
```

If you want to upload it to Docker Hub:

```bash
docker tag image-name username/image-name:version
```

Example

```bash
docker tag secure-ota-server banna/secure-ota-server:v1.0.0
```

---

# Step 5 - Push Image to Docker Hub

Upload the image.

```bash
docker push username/image-name:version
```

Example

```bash
docker push banna/secure-ota-server:v1.0.0
```

This makes the image available online.

---

# Step 6 - Pull Image from Docker Hub

Download an image from Docker Hub.

```bash
docker pull username/image-name:version
```

Example

```bash
docker pull banna/secure-ota-server:v1.0.0
```

---

# Step 7 - Run the Container

Run the Docker container.

```bash
docker run -d \
--name container-name \
-p local-port:container-port \
username/image-name:version
```

Example

```bash
docker run -d \
--name ota-server \
-p 8000:8000 \
banna/secure-ota-server:v1.0.0
```

Parameter explanation

| Parameter | Description                      |
| --------- | -------------------------------- |
| -d        | Run container in background      |
| --name    | Container name                   |
| -p        | Map local port to container port |

---

# Docker Container Management

## Start a Container

```bash
docker start container-name
```

Example

```bash
docker start ota-server
```

---

## Stop a Container

```bash
docker stop container-name
```

Example

```bash
docker stop ota-server
```

---

## List Running Containers

```bash
docker ps
```

---

## List All Containers

```bash
docker ps -a
```

---

## List Local Images

```bash
docker image ls
```

---

# Updating the Latest Tag

Docker Hub automatically displays the **latest** tag as the default version.

If you want another version to become the default, create a new tag and push it.

```bash
docker tag username/image-name:latest username/image-name:v2.0.0
```

Then upload it.

```bash
docker push username/image-name:v2.0.0
```

Now Docker Hub will show the new version alongside the previous ones.

---

# Typical Deployment Workflow

```text
Create Dockerfile
        │
        ▼
docker build
        │
        ▼
docker tag
        │
        ▼
docker login
        │
        ▼
docker push
        │
        ▼
Docker Hub
        │
        ▼
docker pull
        │
        ▼
docker run
        │
        ▼
Running Container
```

---

# Common Docker Commands

| Command         | Description                 |
| --------------- | --------------------------- |
| docker login    | Login to Docker Hub         |
| docker build    | Build an image              |
| docker tag      | Assign a version tag        |
| docker push     | Upload image to Docker Hub  |
| docker pull     | Download image              |
| docker run      | Run a container             |
| docker ps       | Show running containers     |
| docker ps -a    | Show all containers         |
| docker image ls | Show local images           |
| docker stop     | Stop a running container    |
| docker start    | Start an existing container |

---

# Notes

- Always build a new image after modifying your source code.
- Use Semantic Versioning (e.g., `v1.0.0`, `v1.1.0`, `v2.0.0`) for better release management.
- Avoid relying solely on the `latest` tag in production environments.
- Ensure the required firewall port is open before running the container.
- Verify that the local port is not already in use before starting the container.

---

# Example

```bash
docker login

docker build -t secure-ota-server .

docker tag secure-ota-server banna/secure-ota-server:v1.0.0

docker push banna/secure-ota-server:v1.0.0

docker pull banna/secure-ota-server:v1.0.0

docker run -d \
--name ota-server \
-p 8000:8000 \
banna/secure-ota-server:v1.0.0

docker ps
```

The application is now accessible via:

```
http://localhost:8000
```

If deployed on another machine:

```
http://<Server-IPv4>:8000
```
