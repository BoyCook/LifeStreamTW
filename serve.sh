#!/bin/bash
# Serve over HTTP

if [ $# -eq 1 ]
then
    nohup twanager server 127.0.0.1 30080 1> lifestream.log &

else
    twanager server 127.0.0.1 30080
fi
