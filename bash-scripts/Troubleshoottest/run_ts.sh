#!/bin/bash

# Loop until the user enters a valid option: "ping" or "trace"
while true;do 
echo "What type of troubleshoot you need (ping|trace):"
read method
if [ "$method" = "ping" ] || [ "$method" = "trace" ] ;then
	echo "your method is $method "
	break
else
	echo "you have not selected a valid method"
fi 
done

# loop until the user enter the correct file name or quit after three attempts 

attempt=1
maxattempt=3

while true; do
    echo "Select the file name you need to open full path:"
    read filename

    if [ $attempt -le $maxattempt ]; then
        if [ -f "$filename" ]; then
            echo "Your file exists on the system"
            break
        else
            echo "No file named '$filename' exists on the system"
            echo "Attempt $attempt of $maxattempt"
            attempt=$((attempt + 1))
        fi
    else
        echo "You exceeded maximum attempts. Exiting."
        exit 0
    fi
done



