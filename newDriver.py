import json
import random
import heapq
import time as t

def nth_highest_seed(cohort, n):
    # Get the n largest seeds using heapq.nlargest
    largest_seeds = heapq.nlargest(n, cohort.values())

    # Get the nth highest seed from the list of largest seeds
    nth_highest_seed = largest_seeds[-1]

    return nth_highest_seed


def lottery():
    # Define the numbers and their corresponding probabilities
    numbers = [1, 2, 3, 4]
    probabilities = [0.5, 0.25, 0.15, 0.1]

    # Use random.choices() to randomly select a number based on probabilities
    result = random.choices(numbers, weights=probabilities, k=1)[0]
    return result

def get_highest_seed(data_dict):
    # Extract the seeds from the dictionary values
    seeds = [value for value in data_dict.values() if isinstance(value, int)]

    if not seeds:
        raise ValueError("No valid seeds found in the dictionary.")

    # Find the maximum seed
    highest_seed = max(seeds)
    return highest_seed


def get_teams_for_lottery_round(data_dict):
    # Sort the dictionary based on the values (ascending order)
    sorted_data = sorted(data_dict.items(), reverse=True, key=lambda x: x[1])

    # Get the four lowest key-value pairs
    four_lowest = sorted_data[:4]

    # Convert the result back to a dictionary
    result = dict(four_lowest)

    return result


def draft_pick(data_dict, draft_round):
    highest_seed = get_highest_seed(data_dict)

    if draft_round < highest_seed - 2:
        return 1
    else:
        return lottery()

def remove_result_from_standings(standings_state, draft_pick_result):
    # Find the team with the given draft pick result and remove it from the standings
    for team, draft_pick in standings_state.items():
        if draft_pick == draft_pick_result:
            standings_state.pop(team)
            break

def get_team(standings_state, draft_pick_result):
    # Find the team with the given draft pick result and remove it from the standings
    for team, draft_pick in standings_state.items():
        if draft_pick == draft_pick_result:
            return team, draft_pick

def do_lottery(standings):
    draft_round = 14
    standings_state = standings.copy()
    results = {}

    while draft_round > 3:

        draft_cohort = get_teams_for_lottery_round(standings_state)
        draft_pick_result = draft_pick(draft_cohort, draft_round)

        seed = nth_highest_seed(draft_cohort, draft_pick_result)
        team, pick = get_team(standings_state, seed)

        results[team] = pick
        remove_result_from_standings(standings_state, pick)

        draft_round -= 1

    for x in range(3):

        last_team = list(standings_state.items())[-1]
        remove_result_from_standings(standings_state, last_team[1])
        results[last_team[0]] = last_team[1]
    return results

def check_lottery(results):
    for idx, result in enumerate(reversed(results)):
        result_pick = 14 - idx
        seed = 15-results[result]
        seed_difference = seed - result_pick

        if seed_difference > 3:
            raise ValueError("Seed difference is greater than 3")
        if seed_difference < -3:
            raise ValueError("Seed difference is less than 3")

        if seed_difference == 0:
            seed_difference_string = "-"
        else:
            seed_difference_string = f"+{seed_difference}" if seed_difference > 0 else f"{seed_difference}"
        # t.sleep(10)
        print(f"{result_pick}: {result} {seed} ({seed_difference_string})")


draft_round = 14



with open("Standings.json", "r") as f:

    standings = json.load(f)
    res = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
        }

    simulations = 1000000
    print(f"Running {simulations} lottery simulation...")
    for x in range(simulations):
        y = lottery()
        if y in res:
            res[y] += 1
        else:
            res[y] = 1
    for x in res:
        print(f"{x}: {res[x]} ({res[x]/simulations*100}%)")

    print("Running lottery...")
    results = do_lottery(standings)

    check_lottery(results)







