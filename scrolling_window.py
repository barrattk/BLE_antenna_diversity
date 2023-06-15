import serial
import matplotlib.pyplot as plt
from collections import deque

import numpy as np


# Create a deque object to store the data points for the scrolling window
max_data_points = 100  # Adjust this value to change the window size
rssi = deque(maxlen=max_data_points)
channel = deque(maxlen=max_data_points)

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot(rssi)

# Configure the serial port
port = '/dev/ttyACM0'  # Replace with the appropriate serial port
baud_rate = 230400  # Replace with the appropriate baud rate
ser = serial.Serial(port, baud_rate)

keyword = '72076359036375313'


def filter_line(line, keyword):
    if keyword in line and 'Err' not in line:
        # if keyword and not 'Err' in line:
        temp = line.split()
        print(temp)
        rssi = int(temp[2])
        channel = int(temp[3])
        return rssi, channel


# Read and plot live data
while True:
    # Read data from the serial port
    data = ser.readline().decode().strip()  # Adjust the decoding as per your data format

    print(data)
    try:
        rs, ch = filter_line(data, keyword)
    except TypeError:
        continue

    if ch == 38:
        rssi.append(rs)
        # # Update the plot
        # print(rs)
        # print(rssi)
        x = np.arange(0, len(rssi))
        line.set_xdata(x)
        line.set_ydata(list(rssi))

        ax.relim()  # Does not work with collections
        ax.autoscale_view()  # Autoscale the view
        plt.draw()
        plt.pause(0.01)  # Adjust the pause duration as needed
