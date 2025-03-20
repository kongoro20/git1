#!/bin/bash

# URL of the central server that provides the unique link
SERVER_URL="https://4577621e-7112-49f7-b09b-5dead0003f90.deepnoteproject.com/get_item"

# GitHub Token and Gist ID
if [ -f "code.txt" ]; then
    token_part=$(cat code.txt)
    GITHUB_TOKEN="ghp_${token_part}"
else
    echo "Error: 'code.txt' file not found!"
    exit 1
fi

GIST_ID='4d2dae19f71b99b6c38f19d7ef1cdc94'  # Your Gist ID

while true; do
    echo "Requesting item from the server..."
    response=$(curl -s "$SERVER_URL")

    # Extract the item from the JSON response using jq
    item=$(echo "$response" | jq -r .assigned_item)

    # Check if a valid item is received
    if [ "$item" != "null" ] && [ -n "$item" ]; then
        echo "Received item: $item"

        # Copy the item to the clipboard using xclip
        echo -n "$item" | xclip -selection clipboard
        echo "Item copied to clipboard."

        # Extract the filename from the item if it's a URL with filename
        filename=$(basename "${item}")

        # Download the file if it's a URL
        if [[ "$item" =~ ^https?:// ]]; then
            if curl -L -O "$item"; then
                echo "Downloaded: $filename"
            else
                echo "Download failed! Retrying..."
                sleep 5
                continue
            fi

            # Check if a .zip file was downloaded
            if [ ! -f "$filename" ]; then
                echo "No .zip file found after download. Retrying..."
                sleep 5
                continue
            fi

            echo "Downloaded ZIP file: $filename"

            # Unzip the downloaded .zip file into a folder
            UNZIPPED_FOLDER="${filename%.zip}"  # Strip .zip extension
            mkdir -p "$UNZIPPED_FOLDER"
            unzip -o "$filename" -d "$UNZIPPED_FOLDER"

            # Add Firefox preferences and clean up session restore files
            cat <<EOF > "$UNZIPPED_FOLDER/user.js"
user_pref("browser.sessionstore.resume_from_crash", false);
user_pref("browser.startup.page", 0);
user_pref("browser.startup.homepage_override.mstone", "ignore");
user_pref("browser.tabs.warnOnClose", false);
user_pref("browser.warnOnQuit", false);
user_pref("browser.sessionstore.max_tabs_undo", 0);
EOF

            rm -f "$UNZIPPED_FOLDER/sessionstore.js" \
                  "$UNZIPPED_FOLDER/sessionCheckpoints.json" \
                  "$UNZIPPED_FOLDER/recovery.jsonlz4" \
                  "$UNZIPPED_FOLDER/recovery.baklz4"

            # Launch Firefox with the new profile
            nohup firefox --no-remote --new-instance --profile "$UNZIPPED_FOLDER" --purgecaches &

            echo "Firefox launched successfully."
            break  # Exit the loop on success

        else
            echo "Received item is not a URL. Only copied to clipboard."
            break  # Exit the loop
        fi
    else
        echo "No valid item received. Retrying in 5 seconds..."
        sleep 5
    fi
done
