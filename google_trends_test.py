#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 08:36:24 2017

@author: ERIC
"""
from bs4 import BeautifulSoup
from pytrends.request import TrendReq
import requests 
import google_trends_config

#https://stackoverflow.com/questions/6754709/logging-in-to-google-using-python

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content).find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict[google_trends_config.email] = login
        my_dict[google_trends_config.password] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text




# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['Hurricane','Weather'],timeframe='today 1-m',geo='US', gprop='news')

# Interest Over Time
#interest_over_time_df = pytrend.interest_over_time()
#print(interest_over_time_df.head())

# Interest by Region
#interest_by_region_df = pytrend.interest_by_region(resolution='CITY')
#print(interest_by_region_df)

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
#print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df)

# Get Google Keyword Suggestions
#suggestions_dict = pytrend.suggestions(keyword='Butter milk')
#print(suggestions_dict)