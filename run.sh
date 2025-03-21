#!/bin/bash

# Run setup and environment activation
bash setup.sh

# Activate the Python virtual environment
source ./myenv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the virtual environment."
  exit 1
fi

# Prepare environment
touch ~/.Xauthority
pip install pyautogui
pip install --upgrade pillow
pip install opencv-python-headless
pip install pyperclip


# Repeat gofile.sh and github.sh execution 10 times
for i in {1..2}; do
  echo "Execution cycle $i for gofile.sh and github.sh"

  # Run gofile.sh
  bash gofile.sh

  # Check if gofile.sh executed successfully
  if [ $? -ne 0 ]; then
    echo "gofile.sh failed to execute on cycle $i."
    exit 1
  fi

  # Run github.sh
  bash github.sh

  # Check if github.sh executed successfully
  if [ $? -ne 0 ]; then
    echo "github.sh failed to execute on cycle $i."
    exit 1
  fi
  
done

echo "Completed 10 cycles of gofile.sh and github.sh."
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

echo "Completed 5000 runs of navigate.py successfully."
