#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:25:55 2017

Will plot map of traffic or an metric on map of the United States. 

@author: ERIC
"""

import csv

# Opens data file.
filename = '/Users/ERIC/Desktop/geographyPV.csv'

# Create lists for the data we are interested in. Columnbs must have name.
lats, lons = [], []
traffic = []

#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Ignore the header row.
    next(reader)
    
    # Store the latitudes and longitudes in the appropriate lists. 
    # Column 1 is lat. Column 2 is lons. Column 3 is traffic.
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        traffic.append(float(row[2]))
        
#print values to test data.        
print('lats', lats[0:5])
print('lons', lons[0:5])
print('traffic', traffic[0:5])


# Create map using basebamp
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
#Create map dimensions and size. 
eq_map = Basemap(projection='merc', resolution = 'l', area_thresh = 1000.0,
                 llcrnrlon=-126, llcrnrlat=25, urcrnrlon=-67,
                 urcrnrlat=49.5,)
eq_map.drawcoastlines()
eq_map.drawstates()
eq_map.drawcountries()
eq_map.fillcontinents(color = 'lightgrey',lake_color='lightblue')
eq_map.drawmapboundary(fill_color='lightblue')
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 

#Determine marker size
min_marker_size = .0013
for lon, lat, traffic in zip(lons, lats, traffic):
    x,y = eq_map(lon, lat)
    msize = traffic * min_marker_size
    eq_map.plot(x, y, 'ro', markersize=msize, color='green')

#plot map. 
plt.show()
