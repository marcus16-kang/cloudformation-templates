#!/bin/bash

if [ -f /app/binary.pid ]; then
    PID=`cat /app/binary.pid`
    if [ -d /proc/$PID ]; then
        kill -9 $PID
    fi
fi