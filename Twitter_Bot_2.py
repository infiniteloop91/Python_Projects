#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 22:49:33 2017

@author: ERIC
"""

from twython import Twython
import random 
import twitter_config

twitter =Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

RandomNumber = random.randint(1,4)
print(RandomNumber)

if RandomNumber == 1:
    TweetMessage = 'Hello Twitter.' 
    TweetPhoto = '/Users/ERIC/Desktop/Dog_1.jpg'
elif RandomNumber == 2: 
    TweetMessage = 'How are you Today?' 
    TweetPhoto = '/Users/ERIC/Desktop/Dog_2.jpg'
elif RandomNumber == 3:
    TweetMessage = 'I hope you are having a great day.' 
    TweetPhoto = '/Users/ERIC/Desktop/Dog_3.jpg'
elif RandomNumber == 4:
    TweetMessage = 'I am running out of greetings.' 
    TweetPhoto = '/Users/ERIC/Desktop/Dog_4.jpg'

print(TweetMessage)
print(TweetPhoto)


photo = open(TweetPhoto,'rb')
twitter.update_status_with_media(media=photo,status=TweetMessage)
