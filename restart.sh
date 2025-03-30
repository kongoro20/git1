#!/bin/bash

# Start Xvfb if it's not already running
if ! pgrep -x "Xvfb" > /dev/null; then
    echo "Starting Xvfb..."
    Xvfb :1 -screen 0 1366x768x16 &
    sleep 2
fi

# Activate the environment and set necessary variables
sleep 1
source /root/git1/myenv/bin/activate  # Explicit path to myenv
export DISPLAY=:1  # Ensures Firefox uses the correct display
export XAUTHORITY=/root/.Xauthority  # Ensure X server access

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
