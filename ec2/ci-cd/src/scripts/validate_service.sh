#!/bin/bash

for i in $(seq 1 6)
do
    STATUS=$(curl --silent -o /dev/null -w "%{http_code}" "http://127.0.0.1:80/health")

    if [ $STATUS -eq 200 ]; then
        echo "HEALTHCHECK SUCCESS"
        exit 0
    else
        echo "HEALTHCHECK FAILED $STATUS"
        sleep 5
    fi
done

echo "HEALTHCHECK FAILED"
exit 1