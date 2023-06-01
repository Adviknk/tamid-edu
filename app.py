# Advik Nakirikanti
# Python GUI Code

import pandas as pd
import requests
import tkinter as tk
pd.set_option('display.max_columns', None)
import time
import numpy as np

nba_url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2021-22&SeasonType=Regular%20Season&StatCategory=PTS"

r = requests.get(url=nba_url).json()

names = []
points = []

for player in r["resultSet"]["rowSet"]:
    names.append(player[2])
    points.append(player[6])

def show_player():
    player_name = entry.get()
    i = 0
    is_there = True
    for name in names:
        if (player_name == name):
            result.config(text=name + " has " + str(points[i]) + " points per game.")
            is_there = False
        i = i + 1
    if(is_there):
        result.config(text="That player is not part of the top 50.")

# Create the tkinter GUI
root = tk.Tk()
root.geometry("400x200")
root.title("NBA Stats")

# Create widgets
label = tk.Label(root, text="Enter NBA Player Name:")
entry = tk.Entry(root)
button = tk.Button(root, text="Show Player", command=show_player)
result = tk.Label(root, text="")

# Add widgets to the window
label.pack()
entry.pack()
button.pack()
result.pack()

# Run the GUI
root.mainloop()
