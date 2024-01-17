#!/bin/bash
echo "Please wait for the server to be running"

while true; do
    echo ""
    echo ""
    echo "Select an option:"
    echo "1) Create a superuser"
    echo "2) Run tests"
    echo "3) Quit Server"
    read -p "Enter your choice: " choice

    case $choice in
        1)  
            echo ""
            echo ""
            echo "Creating a superuser..."
            docker-compose exec backend python manage.py createsuperuser
            ;;
        2)
            echo ""
            echo ""
            echo "Not implemented yet"
            ;;
        3)
            docker-compose down
            break
            ;;    
        *)
            echo ""
            echo ""
            echo "Invalid option"
            ;;
    esac
done    