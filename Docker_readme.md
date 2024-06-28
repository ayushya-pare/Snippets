## List Docker CLI commands
docker --help

## Display Docker version and info
docker --version
docker info

## Build Docker image
docker build -t <image_name> -f <path_to_Dockerfile> # here -t stands for "tag".
# If Dockerfile is in current work dir
docker build -t <image_name> .

## Start container from Docker image
docker run -ti <image_name> # runs with the command specified at the end of the Dockerfile
docker run -ti <image_name> <cmd> # runs with command cmd.
# note that -t stands for tty and -i for interactive, which you use when you want to interact with the container's
# command line interface (CLI) or run an interactive shell session
#--------------
# Start container with a volume mapping
docker run -v <docker_volume_name>:<path_in_container> -ti <image_name> <cmd>
docker run -v <path_on_host>:<path_in_container> -ti <image_name> <cmd>

## Volumes
# Create a Docker volume
docker volume create <docker_volume_name>

## Log into running container
docker exec -ti <container_name> <cmd>
# Start a bash session in the running container (cmd = bash)
docker exec -ti <container_name> bash
# Start an interactive python session in the container
docker exec -ti <container_name> python
# Execute a python script in the container
docker exec -ti <container_name> python <path_to_py_script>

## List Docker images
docker images
# Remove docker image
docker rmi <image_name>

## List Docker containers (running, all, all in quiet mode)
docker ps
docker ps -a # show stopped or exited containers
docker ps -aq # only returns container ids


## Check logs of running Docker container
docker logs <container_ID>


## Stopping / Removing Killing all container
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker kill $(docker ps -q)

## Cleanup
docker builder prune
docker system prune
docker system prune --volumes
docker container prune
