#!/bin/bash
#先安裝可能缺少的東西
sudo apt-get install xauth -y
xhost +local:docker
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

sudo QT_GRAPHICSSYSTEM="native" docker run -it -e DISPLAY=$DISPLAY -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH chiz0943/ros_noetic

