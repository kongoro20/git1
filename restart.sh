#!/bin/bash

sleep1
source myenv/bin/activate
sleep 3
for i in {1..500}; do
    echo "Running refresh.sh - Attempt $i"
    bash refresh.sh
    sleep 1800
    # Check if the script exited with an error
    if [ $? -ne 0 ]; then
        echo "refresh.sh failed at attempt $i" >&2
        exit 1  # Exit the bash script if navigate.py fails
    fi
done
