#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:51:19 2017

@author: ERIC
"""

#gets exchange rates from api.fixer
#allows you to enter date range
#finds difference in price and percent chage
#all results in terms of US DOLLAR

import requests 
import urllib.parse



def get_exchange_rate():
    
    #set start date and end date
    start_date = '2016-08-23'
    end_date = '2017-08-23'
    print('The Start Date is: ' + start_date)
    print('The End Date is: ' + end_date + '\n')
    
    #creates start date and end date endpoints 
    exchange_url_start = 'http://api.fixer.io/' + start_date + '?' 
    exchange_url_end = 'http://api.fixer.io/' + end_date + '?'
    
    
    #sets base for conversion
    USD = 'USD'
    
    #passes parameter to set base of rate in USD.  Can passover any currency.
    exchange_rate_start =  exchange_url_start + urllib.parse.urlencode({"base": USD})
    #print(exchange_rate_start)

    #gets data
    json_data_exchange_start = requests.get(exchange_rate_start).json()
    #print(json_data_exchange_start)
    
    #gets start rate
    start_GDP = json_data_exchange_start['rates']['GBP']
    print('Start price for the pound is: ' + str(start_GDP))
    
    start_EUR = json_data_exchange_start['rates']['EUR']
    print('Start price for the Euro is: ' + str(start_EUR))
    
    start_RUB = json_data_exchange_start['rates']['RUB']
    print('Start price for the Rupel is: ' + str(start_RUB) + '\n')
    
    exchange_rate_end =  exchange_url_end + urllib.parse.urlencode({"base": USD})
    #print(exchange_rate_end)

    json_data_exchange_end = requests.get(exchange_rate_end).json()
    #print(json_data_exchange_end)
    
    #gets end rate
    end_GDP = json_data_exchange_end['rates']['GBP']
    print('End price for the pound is: ' + str(end_GDP))
    
    end_EUR = json_data_exchange_end['rates']['EUR']
    print('End price for the Euro is: ' + str(end_EUR))
    
    end_RUB = json_data_exchange_end['rates']['RUB']
    print('End price for the Rupel is: ' + str(end_RUB) + '\n')
    
    #gets percent change 
    per_change_GDP = ((end_GDP - start_GDP)/start_GDP)*100
    print('Percent change is for the Pound is: ' + str(round(per_change_GDP, 3)) + '%.')
    
    per_change_EUR = ((end_EUR - start_EUR)/start_EUR)*100
    print('Percent change is for the Euro is: ' + str(round(per_change_EUR, 3)) + '%.')
    
    per_change_RUB = ((end_GDP - start_RUB)/start_RUB)*100
    print('Percent change is for the Rupel is: ' + str(round(per_change_RUB, 3)) + '%.')
get_exchange_rate()    