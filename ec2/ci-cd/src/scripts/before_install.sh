#!/bin/bash

if [ -f /app/binary.pid ]; then
    PID=`cat /app/binary.pid`
    if [ -d /proc/$PID ]; then
        kill -9 $PID
    fi
    rm -f /app/binary.pid
fi

if [ -f /app/binary.log ]; then
    rm -f /app/binary.log
fi

if [ -f /app/binary ]; then
    rm -f /app/binary
fi