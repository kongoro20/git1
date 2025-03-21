#!/bin/bash

# Detect all downloaded profiles that are directories, sorted by modification time (oldest first)
PROFILE_LIST=($(find . -maxdepth 1 -type d -name 'newprofile-*' | sort))

# Check if profiles exist
if [ ${#PROFILE_LIST[@]} -eq 0 ]; then
    echo "Error: No downloaded profiles found!"
    exit 1
fi

echo "Detected ${#PROFILE_LIST[@]} profiles."

# Function to maximize the most recently opened Firefox window
maximize_firefox_window() {
    for i in {1..10}; do  # Retry up to 10 times if needed
        WIN_ID=$(wmctrl -l | grep "Mozilla Firefox" | awk '{print $1}' | tail -n1)
        if [ -n "$WIN_ID" ]; then
            wmctrl -i -r "$WIN_ID" -b add,maximized_vert,maximized_horz
            echo "Maximized Firefox window: $WIN_ID"
            return
        fi
        sleep 1
    done
}

# Loop through each profile dynamically
for PROFILE in "${PROFILE_LIST[@]}"; do
    echo "Opening Firefox with profile: $PROFILE"

    # Ensure Firefox restores the last session
    PREFS_FILE="$PROFILE/user.js"
    echo 'user_pref("browser.sessionstore.resume_session_once", true);' >> "$PREFS_FILE"

    # Open Firefox with the profile
    nohup firefox --no-remote --new-instance --profile "$PROFILE" --purgecaches &

    # Wait for Firefox to open and maximize it
    sleep 7  # Increased to ensure the window is fully loaded
    maximize_firefox_window
    sleep 2  # Extra delay before navigation

    # Run navigate.py script
    echo "Running navigate.py..."
    python3 navigate.py &

    # Wait for navigate.py to complete before proceeding
    wait

    # Close Firefox 2 seconds after navigation
    echo "Closing Firefox in 2 seconds..."
    sleep 2
    while wmctrl -l | grep -i "Mozilla Firefox" >/dev/null; do
        wmctrl -c "Mozilla Firefox"
        sleep 0.5
    done

    # Short pause before opening the next profile
    sleep 3
done
