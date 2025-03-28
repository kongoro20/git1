#!/bin/bash

sleep 1
source /root/git1/myenv/bin/activate  # Explicit path for consistency
export DISPLAY=:1  # Ensure DISPLAY is set
export XAUTHORITY=/root/.Xauthority  # Ensure X server access
sleep 3

for i in {1..500}; do
    echo "Running refresh.sh - Attempt $i" >> /root/restart_out.log
    bash refresh.sh
    sleep 1800  # 30 minutes
    # Check if the script exited with an error
    if [ $? -ne 0 ]; then
        echo "refresh.sh failed at attempt $i" | tee -a /root/restart_err.log
        exit 1  # Exit if refresh.sh fails
    fi
done

echo "restart.sh completed successfully after 500 iterations." >> /root/restart_out.log
