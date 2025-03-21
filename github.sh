#!/bin/bash
# Activate the virtual environment
python script.py
python codespace.py
python boss.py
python newtab.py
python boss.py

sleep 2
while wmctrl -l | grep -i "Mozilla Firefox" >/dev/null; do
        wmctrl -c "Mozilla Firefox"
        sleep 0.5
done

