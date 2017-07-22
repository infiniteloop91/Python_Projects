#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:49:21 2017

@author: ERIC
"""
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()
#enter area code you want to use as a base.
zip = input('Enter the zipcode: ') 
area = search.by_zipcode(zip)
#establish lat and long
Lat = area['Latitude']
Long = area['Longitude']
#check lat and long 
print('This is the Longitude:'+ ' ' + str(Long))
print('This is the Latitude:'+ ' ' + str(Lat))


#find zips within the closests 10 miles of a Lat and Long. 
res = search.by_coordinate(Lat, Long, radius=10, returns=5)



# Print results
count = 0
while (count < 5):
   print('This is within 10 miles:')
   print(res[count])
   count = count + 1


