#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:07:02 2017

Simple number guessing game that uses random and few basic 
statements. 

@author: ERIC
"""

import random

number = random.randint(1,10)

tries = 1

uname = input("Hello, What is your username?\n")

print("Hello", uname + "" ,)

question = input("Would you like to play a game? [Y/N]\n")
if question == "N":
    print("Ok, jog on.")
else:
    print ("Great, I am thinking of a number between 1 & 10")
    guess = int(input("Have a guess:\n"))
    if guess > number:
        print("Try something lower...")
    if guess < number:
        print("Try something higher...")
    while guess != number:
        tries += 1
        guess = int(input("Try again: "))
    else:
        print("You are the best! The nunber was", number, \
        "and it only took", tries, "tries.")
        
    
    