#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:01:48 2019

@author: BradleyCrump


TODO:
    
    Need to write out each lottery pool into a file, and the winning seed as well
    so we can read that file in reverse for a more dramatic reveal
"""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Section 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gotta make that lottery player. A bunch of shit goes down here, so 
pay attention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from random import randint

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



def LotteryTest():
    tester = 0
    first = 0
    second = 0
    third = 0
    fourth = 0
    while tester < 1000000:
        winner = Lottery()
        if winner == 0:
            first += 1
        elif winner == 1:
            second += 1
        elif winner == 2:
            third += 1
        else:
            fourth += 1
        tester += 1
    print("First: ", first)
    print("Second: ", second)
    print("Third: ", third)
    print("Fourth: ", fourth)
    
    
    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Section 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This section opens up the TeamStandings file and reads its contents 
into the program.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time

# Open the file
StandingsFile           = open('TeamStandings.txt', 'r')

# Make an empty league and lottery result
League = []         # A list of each team in the league. Each entry has a name and a standing
LotteryResults = []

# Now add teams to the league
for line in StandingsFile:
    line = line.strip() # Clean up the end of each line
    name, standing = line.split(":") # Split the name and the standing
    
    standing = standing.replace(" ", "") # Get rid of all the whitespace
    team = [name, int(standing)]
    League.append(team)

### NEEDS TO BE FORMATTED
time.sleep(.25)
print("The Selfish Hockey League")
print("-------------------------")
for team in League:
    time.sleep(.25)
    print("Owner: ", team[0], "Standing: ", team[1])

time.sleep(3)
print("\nLottery Testing")
time.sleep(2)
LotteryTest()
time.sleep(5)
"""
Now we have the teams in a data structure, so we need to be able to 'pull out'
four teams into their own structure which represents the current lottery pool.
"""
count = 1
while len(League) > 3:
    time.sleep(1)
    print("\nRound ", count)
    print("----------")
    time.sleep(1)
    LotteryPool = []
    
    firstSeed = League[ (len(League) - 1)] # Gives the worst possible team as the high seed
    print("\nFirst Seed: ",firstSeed)
    time.sleep(.5)
    # Check if this team has shit the bed on every lottery.
    # We do this by comparing the size of the league to the standing of that team
    # The size of the league shrinks by one with every pass through the lottery,
    # so if the standing of the team - 3 is ever larger than the amount of teams
    # remaining, it means that that team has fallen four spots and so they
    # automatically win this round
    
    if (int)(firstSeed[1] - 3) >= len(League):
        #print(League[(len(League)-1)]
        LotteryResults.append(League.pop(len(League)-1)) # take out the team and put it in the Winner
        print("LOSER\n")
        continue # if this was true, start the loop over

    # otherwise get the rest of the teams and do the damn lottery
    
    secondSeed = League[len(League) - 2]
    print("Second Seed: ",secondSeed)
    time.sleep(.5)
    
    thirdSeed = League[len(League) - 3]
    print("Third Seed: ",thirdSeed)
    time.sleep(.5)
    
    fourthSeed = League[len(League) - 4]
    print("Fourth Seed: ",fourthSeed)
    time.sleep(.5)
    
    LotteryPool = firstSeed, secondSeed, thirdSeed, fourthSeed
    
    winner = Lottery()
    winningSeed = LotteryPool[winner]
    
    time.sleep(3)
    print("\nWinning Seed ", winningSeed)
    #print("Index ", League.index(winningSeed))
    index = League.index(winningSeed)
    LotteryResults.append(League.pop(index))
    time.sleep(5)
    i = 0
    while i < 3:
        time.sleep(1)
        print(".")
        i += 1
    count += 1
# Three teams left, pop them off one by one
while len(League) > 0:
    LotteryResults.append(League.pop())


print("\n\nRESULTS\n---------")
for team in LotteryResults:
    print("Team: ", team[0], "\nStanding: ", team[1])
#print(LotteryResults)
#print(len(LotteryResults))

LotteryStandingsFile    = open('LotteryStandings.txt', 'w')
StandingsFile.close()
LotteryStandingsFile.close()