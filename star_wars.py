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
st_names = []
st_height = []
st_mass = []
st_hair_color = []
st_eye_color = []
st_birth_year = []
st_gender = []

        
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
     
        
        count = 0
        while count <= number_of_char:
            #print(json_data['results'][count]['name'])
            st_names.append(json_data['results'][count]['name'])
            st_height.append(json_data['results'][count]['height'])
            st_mass.append(json_data['results'][count]['mass'])
            st_hair_color.append(json_data['results'][count]['hair_color'])
            st_eye_color.append(json_data['results'][count]['eye_color'])
            st_birth_year.append(json_data['results'][count]['birth_year'])
            st_gender.append(json_data['results'][count]['gender'])
            count = count + 1
            
    
#error handling 
    except KeyError:
         #print('Key error \n')
         pass
    except IndexError:
        #print('Index error \n')
        pass


 
#print(st_names) 

guess = input("What character are you looking for: ") 

st_names_set = set(st_names)

# add while true here 
if guess in st_names_set:
    print('Match! ' + guess + ' was found.')
    answer = input('Would you like his or her info? Y or N: \n')
    if answer == 'Y':
        print('Great!')
        index = st_names.index(guess)
        print('Height: ' + st_height[index])
        print('Mass: ' + st_mass[index])
        print('Hair Color: ' + st_hair_color[index])
        print('Eye Color: ' + st_eye_color[index])
        print('Born in: ' + st_birth_year[index])
        print('Height: ' + st_height[index])
        print('Gender: ' + st_gender[index])  
        
       
        #for i in range(len(st_names_set)):
        ## look up character info via index maybe
        ## probably a better way to do this, but this is the first iteration
        
        
    else:
        print('Have a great day!')
    
else:
    print('These are not the droids you are looking for! Please try again.')
 
    






