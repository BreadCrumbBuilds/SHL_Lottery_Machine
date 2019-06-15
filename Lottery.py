#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:48:49 2019

@author: BradleyCrump
"""
from random import randint
# First gets numbers 1 - 50 (50%), second 51 - 75 (25%),
# third 76 - 90 (15%), fourth 91 - 100 (10%)
def Lottery():
    winner = randint(1, 100)
    
    if winner > 0 and winner <= 50:
        return 0
    elif winner > 50 and winner <= 75:
        return 1
    elif winner > 75 and winner <= 90:
        return 2
    else:
        return 3


# Run the lottery 1,000,000 times to verify that it isn't biased
def LotteryTest(numberOfTests):
    output = ''
    test = 0
    first = 0
    second = 0
    third = 0
    fourth = 0
    
    output += "\nLOTTERY TEST\n"    # header
    while test < numberOfTests:
        winner = Lottery()
        if winner == 0:
            first += 1
        elif winner == 1:
            second += 1
        elif winner == 2:
            third += 1
        else:
            fourth += 1
        test += 1
        
    output += '{:<14}'.format("Seed")
    output += '{:<8}'.format("Wins")
    output += '{:>6}'.format("Odds\n")
    output += "--------------------------------"
    
    output += ('{:<14}'.format("\nFirst: ") + 
               '{:<8}'.format(first) + 
               "\t%" + '{:<5.2f}'.format(first/10000))
    
    output += ('{:<14}'.format("\nSecond: ") + 
               '{:<8}'.format(second) + 
               "\t%" + '{:<5.2f}'.format(second/10000))
    
    output += ('{:<14}'.format("\nThird: ") + 
              '{:<8}'.format(third) + 
              "\t%" + '{:<5.2f}'.format(third/10000))
    
    output += ('{:<14}'.format("\nFourth: ") + 
               '{:<8}'.format(fourth) + 
               "\t%" + '{:<5.2f}'.format(fourth/10000))
    
    output += "\n"
    return output
    
    
    