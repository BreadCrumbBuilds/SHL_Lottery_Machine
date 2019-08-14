#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:01:48 2019

@author: BradleyCrump

Finished:
	Read and write the results.
TODO:
	Read back the results in reverse order.
	Make firebase web application
"""
import Lottery as lotto
import Util as util
import DisplayResults as displayResults
"""
Section 1 - Make files to write to
"""
########################################################################
# Files to read and write
StandingsFile = open('./docs/TeamStandings.txt', 'r')
LotteryStandingsFile = open('./docs/LotteryStandings.txt', 'w')
ResultsLog = open('./docs/LotteryResults.txt', 'w')
LottoTestLog = open('./docs/TestLog.txt', 'w')
# End of section 1

"""
Section 2 - Make the Teams from the text file
"""
########################################################################

# Lists to make
League = []
LeagueCopy = []
LotteryResults = []

# Make the League by pulling the text out of Standings.txt
for line in StandingsFile:
    # for is used to loop through something. In this case, we
    # are looping through each line of the Standings file.
    # Each line, we execute the following instructions
    line = line.strip()                     # gets rid of new line characters
    name, standing = line.split(":")        # divides the line into two by :
    standing = standing.replace(" ", "")    # gets rid of extra spaces
    team = [name, int(standing)]            # make a team
    League.append(team)                     # put the team in the league

LeagueCopy = League.copy() 		    # to be used when reading results back

header = ("{0:^20}".format("Owner") + "{:<23}".format("Standing"))
print("\n\n\nWelcome to the Selfish Hockey League Draft Lottery!!!")
util.waitNoDot(3)
print("\nThe Selfish Hockey League 2019 Standings")
util.waitNoDot(3)
print("-----------------------------------------")
util.waitNoDot(.5)
print(header)
for team in League: 	# show the league
    util.waitNoDot(1)
    print('{:<20}'.format(team[0]), '{:^5}'.format(team[1]))

# End of section 2

# Section 3 - Test the Lottery

########################################################################
util.waitNoDot(10)
print("\nLottery Testing 1,000,000 Draws, five times... Five million draws")

LottoTestLog.write("\nLOTTERY TESTING 1,000,000 DRAWs\n")

# Do five tests of the lottery

i = 0
while i < 5:
    string = lotto.LotteryTest(1000000)
    LottoTestLog.write(string)
    print(string)
    util.waitNoDot(3)
    i += 1

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

    # Get the first seed from the league
    firstSeed = League[(len(League) - 1)]
    firstString = "1- " + firstSeed[0] + ": " + str(firstSeed[1]) + "\n"

    ResultsLog.write(firstString)

    # Check if this team has shit the bed on every lottery so far
    # We do this by comparing the size of the league (how many teams
    # are left) to the standing of that team.
    # The size of the league shrinks by one with every pass through the lottery,
    # so if the standing of team - 3 is ever larger than the amount of teams
    # remaining, that team has fallen the maximum four spots, so they
    # automatically win this round
    if (int)(firstSeed[1] - 3) >= len(League):
        # take out the team and put it in the Winner
        LotteryResults.append(League.pop(len(League)-1))
        firstStringLost = "L- " + \
            firstSeed[0] + ": " + str(firstSeed[1]) + "\n"
        ResultsLog.write(firstStringLost)
        count += 1
        continue  # if this was true, start the loop over

    # otherwise get the rest of the teams and do the damn lottery

    secondSeed = League[len(League) - 2]
    secondString = "2- " + secondSeed[0] + ": " + str(secondSeed[1]) + "\n"
    ResultsLog.write(secondString)

    thirdSeed = League[len(League) - 3]
    thirdString = "3- " + thirdSeed[0] + ": " + str(thirdSeed[1]) + "\n"
    ResultsLog.write(thirdString)

    fourthSeed = League[len(League) - 4]
    fourthString = "4- " + fourthSeed[0] + ": " + str(fourthSeed[1]) + "\n"
    ResultsLog.write(fourthString)

    # Put all the teams together in the pool
    LotteryPool = firstSeed, secondSeed, thirdSeed, fourthSeed

    # Find winner
    winner = lotto.Lottery()

    # Get the winning team
    winningSeed = LotteryPool[winner]
    winningString = "W- " + winningSeed[0] + ": " + str(winningSeed[1]) + "\n"
    ResultsLog.write(winningString)

    # Get the index of the winner in the League list (different list than the pool)
    index = League.index(winningSeed)

    # Take the winner out of the League list, and put him in the Results list
    LotteryResults.append(League.pop(index))

    count += 1

# Three teams left
while len(League) > 0:

    # Take them out of the League list in order, put them in results
    header = "Round " + str(count) + "*\n"
    ResultsLog.write(header)

    team = League.pop()
    LotteryResults.append(team)

    teamString = "L- " + team[0] + ": " + str(team[1]) + "\n"
    ResultsLog.write(teamString)

    count += 1

count = 1

LotteryStandingsFile.write("\n\nRESULTS\n---------\n")

header = '{:^24}'.format("Team") + '{:>5}'.format("Seed\n")
header += "---------------------------------------\n"
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

displayResults.run()
