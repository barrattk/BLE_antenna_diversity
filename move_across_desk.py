import matplotlib.pyplot as plt
import numpy as np

# Results from 2023-06-07
# RSSI = [-75, -78, -77, -79, -91, -83,
#         -77, -83, -80, -79, -83, -79]
# dist = np.arange(0, 12) * 10


# Results from 2023-06-13
# Static one is the blue line; Orange one is the mobile anchor
# rssi_static = [-81, -83, -83, -83, -84, -85, -85, -85, -84, -84, -84, -84 ]
# rssi_move = [-83, -86, -80, -84, -81, -79, -82, -94, -81, -81, -86, -83]
#
# dist = [10, 12, 15, 17, 20, 22, 25, 30, 35, 40, 45, 50]

#
# fig = plt.figure()
#
# plt.plot(dist, rssi_static, label='Stationary')
# plt.plot(dist, rssi_move, label='Mobile')
# plt.xlabel('Distance from edge (cm)')
# plt.ylabel('RSSI')
# plt.legend(loc='lower right')
#
# plt.grid()

# Results from 2023-06-14
# Mobile one is the BLUE line; ORANGE one is the STATIC anchor
rssi_static = [-90,-91,-85, -82, -82, -89]
rssi_mobile = [-83,-87,-85, -91, -83, -83]
#
separation = [30, 20, 15, 12, 10, 30]


fig = plt.figure()

markersize =140
fillstyle = 'none'
plt.scatter(separation, rssi_static, marker="x", s=markersize,   edgecolors='Blue', label='Stationary')
plt.scatter(separation, rssi_mobile, marker="*", s=markersize, facecolors=fillstyle, edgecolors='Orange', label='Mobile')
plt.xlabel('Separation (cm)')
plt.ylabel('RSSI')
plt.legend(loc='upper center')

plt.grid()
plt.show()
