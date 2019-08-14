import Util as util
results = open("./docs/LotteryResults.txt", 'r')


def run():

    rawInfo = []
    for line in results:
        rawInfo.append(line)

    index = len(rawInfo) - 1
    round = 14
    reverseOrderList = []

    while index > 0:
        line = rawInfo[index]

        if "L" in line:

            reverseOrderList.append(line[2:])
            print("\n\nDrafting...")
            util.waitNoDot(10)
            print("\n********************************")
            print("Round " + str(round) + "\n" + line[2:])
            util.waitNoDot(3)
            print("\nResults So Far:\n")
            i = 14
            for line2 in reverseOrderList:
                util.waitNoDot(.5)
                print(str(i) + ": " + line2)
                i = i - 1

            round = round - 1
        elif "W" in line:

            reverseOrderList.append(line[2:])
            print("\n\nDrafting...")
            util.waitNoDot(10)
            print("\n********************************")
            print("Round " + str(round) + "\n" + line[2:])
            util.waitNoDot(3)
            print("\nResults So Far:\n")
            i = 14
            for line2 in reverseOrderList:
                util.waitNoDot(.5)
                print("\n" + str(i) + ": " + line2)
                i = i - 1

            round = round - 1
        index = index - 1

    results.close()
