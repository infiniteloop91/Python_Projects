#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:02:56 2017

@author: ERIC
"""

import requests 
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip() #229.00

price_without_symbol = string_price[1:]
price = float(price_without_symbol)
price_str = str(price)

if price < 500:
    print("Buy the chair for " + price_str + ".")
else:
    print("The chair costs too much and is " + price_str + ".")

#https://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328
# <span itemprop="price" class="now-price"> &pound;229.00 </span>
																			

