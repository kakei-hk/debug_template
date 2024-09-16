#!/bin/bash

docker_image_name="debug_template:${USER}"
docker_container_name="debug_template"
workdir="/workspace"

docker run --rm \
    --name ${docker_container_name} \
    -v ${PWD}:${workdir} \
    -it ${docker_image_name} \
    /bin/bash
