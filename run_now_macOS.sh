#!/bin/bash


CURRENT_DIR=$(pwd)
echo "Building the project. Please wait"
docker-compose up --build &
osascript <<EOF
tell application "Terminal"
    do script "cd $CURRENT_DIR; ./aux_run_now.sh"
end tell
EOF