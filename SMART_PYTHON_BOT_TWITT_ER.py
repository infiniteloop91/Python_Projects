#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:11:21 2017

@author: ERIC
"""


  

#import the best module ever
from twython import Twython

#config file is in same directory 
from TWITTER_CONFIG import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

#import keys from config file
twitter =Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def twitter_bot(number_of_tweets):
     topic = input("What do you want to find? ")
     
     
     result = twitter.search(q=topic, count=number_of_tweets)
     
     retweet_message = input("What would you like the message to be? ")

     for i in result['statuses']:
         print(i['text'].encode('ascii', 'ignore'))
         tweet_id = i['id']
         print(id)
         twitter.create_favorite(id=tweet_id)
         twitter.retweet(id=tweet_id)
         twitter.update_status(status=retweet_message, in_reply_to_status_id=tweet_id)
         
twitter_bot()
    
  
    
    #print(i['entities']['user_mentions'])
    

#photo = open(TweetPhoto,'rb')
#twitter.update_status_with_media(media=photo,status=TweetMessage)
