#!/usr/bin/env bash

export IMAGE=$1
docker run -d -p 81:81 --name ${IMAGE}
echo "success"
