import serial
import matplotlib.pyplot as plt
from collections import deque

import numpy as np
# Used with programming files from Ian that alternate the blinks between channel 37, 38 and 39
# Respectively colors are blue, oragnge and green.(Yes I should have done a legend)

# Create a deque object to store the data points for the scrolling window
max_data_points = 200  # Adjust this value to change the window size
rssi37 = deque(maxlen=max_data_points)
rssi38 = deque(maxlen=max_data_points)
rssi39 = deque(maxlen=max_data_points)
rssi = deque(maxlen=max_data_points)
channel = deque(maxlen=max_data_points)

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line37, = ax.plot(rssi37)    # Will end up being BLUE
line38, = ax.plot(rssi38)   # Will end up being ORANGE
line39, = ax.plot(rssi39)   # Will end up being GREEN
# Configure the serial port
port = '/dev/ttyACM0'  # Replace with the appropriate serial port
baud_rate = 230400  # Replace with the appropriate baud rate
ser = serial.Serial(port, baud_rate)

keyword = '72076359036375313'


def filter_line(line, keyword):
    if keyword in line and 'Err' not in line:
        # if keyword and not 'Err' in line:
        temp = line.split()
        # print(temp)
        rssi = int(temp[2])
        channel = int(temp[3])
        return rssi, channel
#
# def update_plot(ax,  rssi):



# Read and plot live data
while True:
    # Read data from the serial port
    data = ser.readline().decode().strip()  # Adjust the decoding as per your data format

    # print(data)
    try:
        rs, ch = filter_line(data, keyword)
    except TypeError:
        continue

    if ch == 37:
        rssi37.append(rs)
        # # Update the plot
        # print(rs)
        # print(rssi)
        x = np.arange(0, len(rssi37))
        line37.set_xdata(x)
        line37.set_ydata(list(rssi37))

    if ch == 38:
        rssi38.append(rs)
        # # Update the plot
        # print(rs)
        # print(rssi)
        x = np.arange(0, len(rssi38))
        line38.set_xdata(x)
        line38.set_ydata(list(rssi38))

    if ch == 39:
        rssi39.append(rs)
        # # Update the plot
        # print(rs)
        # print(rssi)
        x = np.arange(0, len(rssi39))
        line39.set_xdata(x)
        line39.set_ydata(list(rssi39))
    ax.relim()  # Does not work with collections
    ax.autoscale_view()  # Autoscale the view
    plt.draw()
    plt.pause(0.01)  # Adjust the pause duration as needed
