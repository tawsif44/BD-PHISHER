# Dockerfile
# Author       : tawsif44
# Github       : https://github.com/tawsif44
# Date         : 17-12-2023
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/tawsif44/BD-PHISHER"

# Working directory
WORKDIR /BD-Phisher/
# Add files 
ADD . /BD-Phisher

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip php openssh-client -y
RUN pip3 install -r files/requirements.txt --break-system-packages
RUN apt-get clean

# Main command
CMD ["python3", "bdphisher.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t tawsif44/bdphisher:latest", "sudo docker run --rm -it kasroudra/bdphisher:latest"

## "sudo docker pull tawsif44/bdphisher", "sudo docker run --rm -it tawsif44/bdphisher"
