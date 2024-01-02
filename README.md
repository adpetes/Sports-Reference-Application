# Sports-Reference-Application
Sports Reference application question - engineering prompt

My solutions first reads a json file as input into teams_data, which is a nested Python dictionary.

I create a matrix using a Pandas dataframe because dataframes allow for named rows (indices) and columns which matches the format of the example table provided when printed.

I iterate through over each team (keys in the dictionary), and iterate over each team again in a nested loop. Since the Json file takes this format: 'BRO': {'BSN': {'W': 10, 'L': 12}, ..., I retrieve the number of wins for a given matchup between team1 and team2 by doing: teams_data[team1][team2]['W'].

Finally, I print the matrix. The example input prints this:

    BRO BSN CHC CIN NYG PHI PIT STL
BRO  --  10  15  15  14  14  15  11
BSN  12  --  13  13  13  14  12   9
CHC   7   9  --  12   7  16   8  10
CIN   7   9  10  --  13  13  13   8
NYG   8   9  15   9  --  12  15  13
PHI   8   8   6   9  10  --  13   8
PIT   7  10  14   9   7   9  --   6
STL  11  13  12  14   9  14  16  --
