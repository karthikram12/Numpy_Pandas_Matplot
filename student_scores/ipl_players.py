import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_players_csv = pd.read_csv('deliveries.csv')
ipl_data = pd.DataFrame(ipl_players_csv)

ipl_teams = pd.Series(pd.Index(ipl_data['batting_team']).union(pd.Index(ipl_data['bowling_team']))).unique()
ipl_batsmen_list = pd.Series(ipl_data['batsman']).unique()
match_id = pd.Series(ipl_data['match_id']).unique()

total_score_by_team = ipl_data.groupby('batting_team')['total_runs'].sum()
total_score_by_players = ipl_data.groupby(['batsman'])['total_runs'].sum(numeric_only=True).sort_values(ascending=False)
number_of_balls_faced_by_team = ipl_data['batting_team'].value_counts()
matches_played_by_teams = (ipl_data.groupby('batting_team')['match_id'].nunique().sort_values(ascending=False))
average_score_by_teams = total_score_by_team/matches_played_by_teams
matches_played_by_players = (ipl_data.groupby('batsman')['match_id'].nunique().sort_values(ascending=False))
average_score_by_players = (total_score_by_players / matches_played_by_players).sort_values(ascending=False)
player_zscore = ((total_score_by_players - total_score_by_players.values.mean()) / total_score_by_players.values.std()).sort_values(ascending=False)
print(player_zscore)

#plt.bar(ipl_teams,total_score_by_team.values, color='blue')

matches_played_by_players = ipl_data.groupby('batsman')['match_id'].nunique().sort_values(ascending=False)
print(matches_played_by_players)
print(total_score_by_players)
top_five_scorers = list(total_score_by_players.sort_values(ascending=False).head(5).index)
print(top_five_scorers)

#plt.plot(matches_played_by_players.head(5).index, average_score_by_players.head(5).values)
plt.scatter(matches_played_by_players.values, total_score_by_players.values)
plt.show()







