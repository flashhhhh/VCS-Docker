# Docker Documentation

## Overview
Docker is a platform for developing, packaging, and running applications in isolated environments called **containers**. Containers encapsulate all dependencies, making applications portable and consistent across different environments.

## Docker Architecture

Docker follows a client-server architecture:

- **Docker Client**: The primary interface for users to interact with Docker. Commands like `docker run` are sent from the client to the Docker daemon.
- **Docker Daemon (`dockerd`)**: Handles building, running, and managing containers, images, networks, and volumes. It listens for API requests and can communicate with other daemons.
- **Docker Registries**: Repositories for storing and distributing Docker images. The default public registry is Docker Hub, but private registries are also supported.

## Key Concepts

### Image
A Docker image is a read-only template with instructions for creating a container. Images are often based on other images and can be customized with additional layers.

### Container
A container is a runnable instance of an image. It includes the application and all its dependencies. Containers can be started, stopped, and removed independently.

### Volume
Volumes provide persistent storage for containers. They allow data to persist even if the container is deleted and can be shared between multiple containers.

### Network
Docker networks enable communication between containers. Containers can be attached to one or more networks to facilitate inter-container communication.

### Docker Compose
Docker Compose is a tool for defining and running multi-container Docker applications. Using a YAML file, you can configure services, networks, and volumes, and start all services with a single command (`docker-compose up`).

## Building Images
Docker images are typically built using a `Dockerfile`, which contains a set of instructions for assembling the image. Use the `docker build` command to create an image from a `Dockerfile`.

### Example Dockerfile
```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]
```
### Build Command
```bash
docker build -t myapp:latest .
```
## Running Containers
To run a container from an image, use the `docker run` command. You can specify options like port mapping, environment variables, and volume mounts.
### Example Run Command
```bash
docker run -d -p 8080:80 --name myapp-container myapp:latest
```
## Managing Containers
### Common Commands
- `docker ps`: List running containers.
- `docker ps -a`: List all containers (running and stopped).
- `docker stop <container_id>`: Stop a running container.
- `docker start <container_id>`: Start a stopped container.
- `docker rm <container_id>`: Remove a stopped container.
- `docker logs <container_id>`: View logs for a container.
- `docker exec -it <container_id> <command>`: Execute a command inside a running container.
## Networking
Docker provides several networking options to connect containers:
- **Bridge Network**: The default network type, allowing containers to communicate on the same host.
- **Host Network**: Shares the host's network stack, allowing containers to use the host's IP address.
- **Overlay Network**: Used for multi-host networking, allowing containers on different hosts to communicate.
- **Macvlan Network**: Assigns a MAC address to a container, making it appear as a physical device on the network.
## Docker Compose Example
### `docker-compose.yml`
```yaml
version: '3'
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
  app:
    build: .
    volumes:
      - ./app:/app
    depends_on:
      - web
  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db_data:/var/lib/postgresql/data
volumes:
  db_data:
```
### Start Services
```bash
docker-compose up -d
```

## Docker Registry
Docker images can be stored in a registry. The default public registry is Docker Hub, but you can also set up private registries.
### Pushing an Image to Docker Hub
```bash
docker login
docker tag myapp:latest myusername/myapp:latest
docker push myusername/myapp:latest
```
### Pulling an Image from Docker Hub
```bash
docker pull myusername/myapp:latest
```

## Docker Security
Docker security involves several best practices to ensure the safety of your containers and images:
- **Use Official Images**: Start with official images from Docker Hub to ensure they are maintained and secure.
- **Keep Images Updated**: Regularly update your images to include the latest security patches.
- **Limit Container Privileges**: Run containers with the least privileges necessary. Use the `--user` flag to specify a non-root user.
- **Use Docker Secrets**: For sensitive data like passwords, use Docker secrets instead of environment variables.
- **Network Isolation**: Use Docker networks to isolate containers and control communication between them.

## Docker CLI Reference
### Common Commands
- `docker version`: Show Docker version information.
- `docker info`: Display system-wide information about Docker.
- `docker images`: List all available images on the local machine.
- `docker rmi <image_id>`: Remove an image from the local machine.
- `docker network ls`: List all Docker networks.
- `docker volume ls`: List all Docker volumes.

## Docker Swarm
Docker Swarm is Docker's native clustering and orchestration tool. It allows you to manage a cluster of Docker engines as a single virtual system, enabling high availability and scalability for your applications.
### Key Features
- **Service Discovery**: Automatically discovers services in the swarm.
- **Load Balancing**: Distributes incoming requests across multiple service instances.
- **Scaling**: Easily scale services up or down by adjusting the number of replicas.
- **Rolling Updates**: Update services with zero downtime by rolling out changes gradually.
### Initializing a Swarm
```bash
docker swarm init
```
### Deploying a Service in Swarm
```bash
docker service create --name myservice --replicas 3 -p 8080:80 nginx:latest
```
### Managing Swarm Services
```bash
docker service ls  # List all services in the swarm
docker service ps myservice  # List tasks for a specific service
docker service update --image nginx:latest myservice  # Update a service
docker service scale myservice=5  # Scale a service to 5 replicas
```