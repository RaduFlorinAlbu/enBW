#!/bin/bash

# Store the current directory
CURRENT_DIR=$(pwd)

echo "Building the project. Please wait"
docker-compose up --build &
gnome-terminal -- bash -c "cd '$CURRENT_DIR'; ./aux_run_now.sh; exec bash"

