import pandas as pd
import random

# functionalise initialisation
# add in boat type/ differnt boat number
# next round generator improvement

# initialize:
teams = []
for i in range(1, 37):
    teams.append('team'+str(i))
print(teams)

results = pd.DataFrame(teams, columns=['Teams'])
result = [0] * len(results)
results['score'] = result
print(results)


def next_round_generator(teams):
    round_team1 = []
    round_team2 = []
    for j in range(0, 35, 2):
        round_team1.append(teams[j])
        round_team2.append(teams[j+1])
        next_round = pd.DataFrame(round_team1, columns=['firstteam'])
        next_round['secondteam'] = round_team2
    print(next_round)
    return next_round


def random_results_generator(n):
    results = []
    for race in range(n):
        ordered = [z for z in range(10, 16)]
        random.shuffle(ordered)
        results.append(ordered)
    return results


def team_results(result):
    team1 = [10, 11, 12]
    team2 = [13, 14, 15]
    team1_result = []
    team2_result = []
    for i, r in enumerate(result):
        if r in team1:
            team1_result.append(i+1)
        if r in team2:
            team2_result.append(i+1)
    return team1_result, team2_result


def all_results(round):
    team1_results = []
    team2_results = []
    for race_result in random_results_generator(len(round)):
        print(race_result)
        team1_result, team2_result = team_results(race_result)
        team1_results.append(team1_result)
        team2_results.append(team2_result)
    round['team1_score'] = team1_results
    round['team2_score'] = team2_results
    return round


def update_results(current_results, round_results):
    for i, row in round_results.iterrows():
        if sum(row['team1_score']) < 11:
            winner = row['firstteam']
            ind = teams.index(winner)
            winner_current_score = results.iloc[ind].score
            winner_current_score += 1
            results.at[ind, 'score'] = winner_current_score
        else:
            winner = row['secondteam']
            ind = teams.index(winner)
            winner_current_score = results.iloc[ind].score
            winner_current_score += 1
            results.at[ind, 'score'] = winner_current_score
    print(results)
    return results


def complete_round(teams, results):
    round = next_round_generator(teams)
    round = all_results(round)
    results = update_results(results, round)
    sorted_results = results.sort_values(by=['score'], ascending=False)
    print(sorted_results)

    teams = list(sorted_results['Teams'])
    next_round = next_round_generator(teams)
    print('Next Round', next_round)
    return sorted_results


def run_simulation(number_of_rounds):
    for n in range(number_of_rounds):
        sorted_results = complete_round(teams, results)
    return sorted_results


number_of_rounds = 20
results = run_simulation(number_of_rounds)
print(results)