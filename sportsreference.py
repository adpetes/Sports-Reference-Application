import json
import pandas as pd

with open('sportsreferenceques.json', 'r') as file:
    teams_data = json.load(file)

teams = teams_data.keys()
h_to_h_matrix = pd.DataFrame(index=teams, columns=teams)

for team in teams_data.keys():
    for opp in teams_data.keys():
        if (team == opp): 
            h_to_h_matrix.loc[team][opp] = '--'
        else:
            h_to_h_matrix.loc[team][opp] = teams_data[team][opp]['W']

print(h_to_h_matrix)
