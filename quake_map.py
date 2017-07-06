#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 23:45:31 2017

Tutorial via http://introtopython.org/visualization_earthquakes.html

@author: ERIC
"""
import csv

# Open file.
file = '/Users/ERIC/Desktop/1.0_hour.csv'

# Create empty lists.
lats, lons = [], []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(file) as f:
    # Create a csv object.
    reader = csv.reader(f)
    
    # Ignore header.
    next(reader)
    
    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))
        
# Print first 5 lats and lons.
print('lats', lats[0:5])
print('lons', lons[0:5])


#Import Map Tools
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


#make Map 
map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'green')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
 
x,y = map(lons, lats)
map.plot(x, y, 'ro', markersize=6)

# Plot map.
plt.show()