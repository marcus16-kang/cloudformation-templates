#!/bin/bash

nohup /app/binary > /app/binary.log 2>&1 & echo $! > /app/binary.pid