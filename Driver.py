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
import Lottery as lotto
import Util as util

"""
Section 1 - Make files to write to
"""
########################################################################
# Files to read and write
StandingsFile           = open('./docs/TeamStandings.txt', 'r')
ResultsLog              = open('./docs/LotteryResults.txt', 'w')
LottoTestLog            = open('./docs/TestLog.txt', 'w')
# End of section 1

"""
Section 2 - Make the Teams from the text file
"""
########################################################################

# Lists to make
League = []
LotteryResults = []

# Make the League
for line in StandingsFile:
    line = line.strip()                     # gets rid of new line characters
    name, standing = line.split(":")        # divides the line into two by :
    standing = standing.replace(" ", "")    # gets rid of extra spaces
    team = [name, int(standing)]            # make a team
    League.append(team)                     # put the team in the league


header = ("{0:^20}".format("Owner") + "{:<23}".format("Standing"))
print("\nThe Selfish Hockey League 2019 Standings")
print("-----------------------------------------")
print(header)

for team in League:
    print('{:<20}'.format(team[0]), '{:^5}'.format(team[1]))

# End of section 2

"""
Section 3 - Test the Lottery

########################################################################
print("\nLottery Testing")

LottoTestLog.write("\nLOTTERY TESTING\n")

# Do five tests of the lottery

i = 0
while i < 5:  
    string = lotto.LotteryTest(1000000)
    LottoTestLog.write(string)
    print(string)
    #util.wait(3)
    i += 1
"""
# End of section 3

"""
Section 4 - Do the lottery, save the results into a Log file
to be read in later
"""
########################################################################

count = 1

# Do the lotto: 4 teams at a time, until there are 3 teams left
while len(League) > 3:  # run until only three teams left

    # Initialize temporary list to store each round of lottery
    LotteryPool = []
    
    # Make and write header
    header = "Round " + str(count) + "*\n"
    ResultsLog.write(header)
    print(header)
    
### FORMATTED UNTIL HERE
    # Get the first seed from the league
    firstSeed = League[ (len(League) - 1)]
    
    firstString = "1- " + firstSeed[0] + ": " + str(firstSeed[1])
    ResultsLog.write(firstString)
    print(firstString)
 
    # Check if this team has shit the bed on every lottery so far
    # We do this by comparing the size of the league to the standing of that team
    # The size of the league shrinks by one with every pass through the lottery,
    # so if the standing of team - 3 is ever larger than the amount of teams
    # remaining, that team has fallen the maximum four spots, so they
    # automatically win this round
    
    if (int)(firstSeed[1] - 3) >= len(League):
        #print(League[(len(League)-1)]
        LotteryResults.append(League.pop(len(League)-1)) # take out the team and put it in the Winner
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
    winner = lotto.Lottery()
    
    # Get the winning team
    winningSeed = LotteryPool[winner]
    
    print("\nWinning Seed ", winningSeed, "\n")

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

LotteryStandingsFile    = open('LotteryStandings.txt', 'w')

LotteryStandingsFile.write("\n\nRESULTS\n---------\n")

header = '{:^24}'.format("Team") + '{:>5}'.format("Seed\n")
header+= "---------------------------------------\n"
LotteryStandingsFile.write(header)

for team in LotteryResults:

    LotteryStandingsFile.write('{:<4}'.format("#" + (str(count))) + '| ' +  
                               '{:<20}'.format(str(team[0])) + "| "
                               '{:<5}'.format(str(team[1])) + "\n")
    count += 1

StandingsFile.close()
ResultsLog.close()
LotteryStandingsFile.close()
LottoTestLog.close()
