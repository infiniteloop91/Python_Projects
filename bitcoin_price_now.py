#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:03:12 2017

@author: ERIC
"""



import requests 



def get_bitcoin_price():
    price_api = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    url = price_api 

    #if adding query string + urllib.parse.urlencode({"address": address})

    json_data = requests.get(url).json()
    #print(json_data)

    update_time = str(json_data['time']['updated'])
    print('Updated on: ' + update_time)

    json_status = json_data['disclaimer']
    #print('Disclaimer:' + json_status)

    US_Price = json_data['bpi']['USD']['rate']
    US_Price_string = str(US_Price)
    print('The US Rate is: ' + US_Price_string)

    US_Price = json_data['bpi']['GBP']['rate']
    US_Price_string = str(US_Price)
    print('The GBP Rate is: ' + US_Price_string)

    US_Price = json_data['bpi']['EUR']['rate']
    US_Price_string = str(US_Price)
    print('The EURO Rate is: ' + US_Price_string)
get_bitcoin_price()