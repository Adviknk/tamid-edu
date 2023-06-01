# Advik Nakirikanti
# Small API integration with NBA stats


# change

import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np

nba_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2021-22&SeasonType=Regular%20Season&StatCategory=PTS"

r = requests.get(url=nba_url).json()


names = []
points = []
i = 0
is_there = True

for player in r["resultSet"]["rowSet"]:
    names.append(player[2])
    points.append(player[6])

player_name = input("Enter NBA Player Name: ")

for name in names:
    if (player_name == name):
        print(name + " has " + str(points[i]) + " points per game.")
        is_there = False
    i = i + 1

if(is_there):
    print("That player is not part of the top 50.")