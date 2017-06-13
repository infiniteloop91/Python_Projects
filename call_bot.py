#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:38:52 2017
From Matt Makai's great tutorial via https://www.fullstackpython.com

@author: ERIC
"""
from twilio.rest import Client


""" Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
 and use the E.164 format, for example: "+12025551234"
"""

TWILIO_PHONE_NUMBER = "+YOURTWILIONUMBER"

# Add number or numbers you want to dial as comma separated. 
DIAL_NUMBERS = ["+NUMBERYOUWANTTOCALL,+NUMBERYOUWANTTOCALL2"]

# URL location of TwiML instructions Matt Makai made this one. 
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# I would probably make this a separate config file. 
client = Client("SID", "TOKEN")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number. For loop dials
    each number in dial_number. Then prints if number is sucessfully dialed. FYI:
        must upgrade account to dial non-verified numbers, but still a great tutorial"""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)