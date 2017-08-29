#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:20:49 2017

@author: ERIC
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint 

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('cts').sheet1
  
pp = pprint.PrettyPrinter()
# sheet.cell (row, column).value                
results = sheet.cell(6, 1).value
#results = sheet.get_all_records()

#sheet.update(row, column) updates info
pp.pprint(results)

#row = ["I am", "Updating", "This row", "With a", "Function"]
#index = row value
#sheet.insert_row(row, index)     

#sheet.delete_row (index number)            