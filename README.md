# Sports-Reference-Application
Sports Reference application question - engineering prompt

My solutions first reads a json file as input into teams_data, which is a nested Python dictionary.

I create a matrix using a Pandas dataframe because dataframes allow for named rows (indices) and columns which matches the format of the example table provided when printed.

I iterate through over each team (keys in the dictionary), and iterate over each team again in a nested loop. Since the Json file takes this format: 'BRO': {'BSN': {'W': 10, 'L': 12}, ..., I retrieve the number of wins for a given matchup between team1 and team2 by doing: teams_data[team1][team2]['W'].

Finally, I print the matrix. The example input prints this:

![image](https://github.com/adpetes/Sports-Reference-Application/assets/39361831/c80fa63b-c8b3-466d-bd9b-e33c7ffc3c60)
