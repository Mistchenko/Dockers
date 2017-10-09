#!/bin/sh
# ---------------------------------------------------------------------
# docker run
# ---------------------------------------------------------------------
#docker run --rm --name CO7 -it co7py27 sh

#docker run --rm --name CO7 -v /home/mist/Dockers/co7py27/app/:/var/app -it co7py27 sh

docker run --rm --name CO7 -v $(pwd)/app/:/var/app -it co7py27 sh
