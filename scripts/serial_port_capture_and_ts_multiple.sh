#!/bin/bash

outfile_pre=$1

if [ -z "$outfile_pre" ]; then
  echo "Outfile prefix not provided... exiting"
  exit 1
else
  echo "Using Output Prefix: $outfile_pre"
fi


# Prompt the user with a yes/no question
read -p "Do you want to continue (y/n)? " answer




# femtocom /dev/ttyUSB0 230400 | ts '[%Y-%m-%d %H:%M:%S]' | tee ./output.txt
#
# Timestamp as the number of seconds since the Epoch
# femtocom /dev/ttyACM0 230400 | ts '[%.s]' | tee $outfile
# femtocom /dev/ttyUSB0 230400 | ts '[%.s]' | tee $outfile

# Check the user's response
if [[ $answer =~ ^[Yy]$ ]]; then
    echo "Continuing with the script..."

    for ((i=0; i<=5; i++))
    do
        port="/dev/ttyACM${i}"
        if [[ -e $port ]]; then
            echo "Valid serial port found: $port"

            outfile=$outfile_pre"-"${i}".txt"
            echo -e $outfile


            # You can add additional actions here, such as configuring the serial port settings
            # femtocom /dev/ttyACM${i} 230400 | ts '[%.s]' | tee $outfile &
            gnome-terminal -- bash -c "femtocom /dev/ttyACM${i} 230400 | ts '[%.s]' | tee $outfile"
          else
            echo "Serial port not found: $port"
        fi
    done


else
  echo "Exiting the script."
  exit 0
fi
