#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:01:48 2019

@author: BradleyCrump


TODO:
    
    ø Need to write out each lottery pool into a file, and the winning 
    seed as well so we can read that file in reverse for a more 
    dramatic reveal
    ø Remove all the sleeps
    ø Format the testing 
    ø Modularize classes: Lottery
"""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Section 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gotta make that lottery player. A bunch of shit goes down here, so 
pay attention
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
    test = 0
    first = 0
    second = 0
    third = 0
    fourth = 0
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
    
    # Clean up the end of each line by taking away the extra newline character
    line = line.strip() 
    
    # Split the name and the standing apart
    name, standing = line.split(":")
    
    # Get rid of all the whitespace
    standing = standing.replace(" ", "") 

    # a single team has a name and a standing
    team = [name, int(standing)] 
    League.append(team)

### NEEDS TO BE FORMATTED

print("The Selfish Hockey League")
print("-------------------------")

for team in League:
    print("Owner: ", team[0], "Standing: ", team[1])


print("\nLottery Testing")

LotteryTest(1000000)

"""
Now we have the teams in a data structure, so we need to be able to 'pull out'
four teams into their own structure which represents the current lottery pool.
"""


count = 1
while len(League) > 3: # do this over and over again until there are only 3 teams left

    print("\nRound ", count)
    print("----------")

    LotteryPool = []
    
    firstSeed = League[ (len(League) - 1)] # Gives the worst possible team as the high seed
    print("\nFirst Seed: ",firstSeed)
 
    # Check if this team has shit the bed on every lottery so far
    # We do this by comparing the size of the league to the standing of that team
    # The size of the league shrinks by one with every pass through the lottery,
    # so if the standing of team - 3 is ever larger than the amount of teams
    # remaining, that team has fallen the maximum four spots, so they
    # automatically win this round
    
    if (int)(firstSeed[1] - 3) >= len(League):
        #print(League[(len(League)-1)]
        LotteryResults.append(League.pop(len(League)-1)) # take out the team and put it in the Winner
        print("LOSER\n")
        count+=1
        continue # if this was true, start the loop over

    # otherwise get the rest of the teams and do the damn lottery
    
    secondSeed = League[len(League) - 2]
    print("Second Seed: ",secondSeed)
    
    thirdSeed = League[len(League) - 3]
    print("Third Seed: ",thirdSeed)
    
    fourthSeed = League[len(League) - 4]
    print("Fourth Seed: ",fourthSeed)

    # Put all the teams together in the pool
    LotteryPool = firstSeed, secondSeed, thirdSeed, fourthSeed
    
    # Find winner
    winner = Lottery()
    
    # Get the winning team
    winningSeed = LotteryPool[winner]
    
    print("\nWinning Seed ", winningSeed)

    # Get the index of the winner in the League list (different list than the pool)
    index = League.index(winningSeed)
    
    # Take the winner out of the League list, and put him in the Results list
    LotteryResults.append(League.pop(index))
    
    count += 1

# Three teams left
while len(League) > 0:
    
    # Take them out of the League list in order, put them in results
    LotteryResults.append(League.pop())

count = 1
print("\n\nRESULTS\n---------")
for team in LotteryResults:
    print("#", count, team[0], " ", team[1])
    count += 1


LotteryStandingsFile    = open('LotteryStandings.txt', 'w')
StandingsFile.close()
LotteryStandingsFile.close()
