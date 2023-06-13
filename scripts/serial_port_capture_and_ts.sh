#!/bin/bash

outfile=$1

if [ -z "$outfile" ]; then
  echo "Outfile not provided... exiting"
  exit 1
else
  echo "Using Output file: $outfile"
fi


# Prompt the user with a yes/no question
read -p "Do you want to continue (y/n)? " answer

# Check the user's response
if [[ $answer =~ ^[Yy]$ ]]; then
    echo "Continuing with the script..."


    # femtocom /dev/ttyUSB0 230400 | ts '[%Y-%m-%d %H:%M:%S]' | tee ./output.txt
    #
    # Timestamp as the number of seconds since the Epoch
    femtocom /dev/ttyACM0 230400 | ts '[%.s]' | tee $outfile
    # femtocom /dev/ttyUSB0 230400 | ts '[%.s]' | tee $outfile

else
  echo "Exiting the script."
  exit 0
fi
