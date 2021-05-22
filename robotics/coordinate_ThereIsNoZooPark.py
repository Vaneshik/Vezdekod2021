import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import time


def callback_start(i):
    long = df.get('start station longitude')
    lat = df.get('start station latitude')
    coors = list(set(zip(df.get('start station longitude'), df.get('start station latitude'), df.get('start station name'))))
    for i in coors:
        plt.text(i[1], i[0], '1')
    print(1)
    plt.draw()

df = pd.read_csv('nyc_robots.csv', sep=';')
ruh_m = plt.imread('map.png')
BBox = (-74.1263, -73.9575, 40.6828, 40.7875)

print(BBox)


plt.plot(df.get('end station longitude'), df.get('end station latitude'), '.r', markersize=5)
plt.plot(df.get('start station longitude'), df.get('start station latitude'), '.g', markersize=5)

plt.axis([BBox[0], BBox[1], BBox[2], BBox[3]])
plt.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')

coors = list(set(zip(df.get('start station longitude'), df.get('start station latitude'), df.get('start station name'))))
for i in coors:
    print(i[0], i[1])
    plt.text(i[0], i[1], i[2], fontsize=7)
coors = list(set(zip(df.get('end station longitude'), df.get('end station latitude'), df.get('end station name'))))
for i in coors:
    print(i[0], i[1])
    plt.text(i[0], i[1], i[2], fontsize=7)

plt.axes([0, 0, 0, 0])

plt.show()
