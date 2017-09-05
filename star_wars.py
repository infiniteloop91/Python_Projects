#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:52:33 2017

@author: ERIC
"""

import requests 
import urllib.parse

#number of pages in JSON feed
page_list = [1,2,3,4,5,6,7,8,9]
        
for i in range(len(page_list)):
    try:
        pages = page_list[i]
        
        endpoint = "https://swapi.co/api/people/?"
        
        type = 'json'
        
        #specifies api parameters
        url = endpoint + urllib.parse.urlencode({"format": type, "page": pages})
        #print(url_2)
        
        #gets info
        json_data = requests.get(url).json()
        number_of_char = json_data['count']
        
        #list to store names
        st_names = []
        
        count = 0
        while count <= number_of_char:
            print(json_data['results'][count]['name'])
            st_names.append([json_data['results'][count]['name']])
            count = count + 1
            
        
        
#error handling 
    except KeyError:
         print('Key error \n')
         pass
    except IndexError:
        print('Index error \n')
        pass
       