# Advik Nakirikanti

# App with 2 APIS

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
root.title("Sports Statistics")

# Create widgets
label = tk.Label(root, text="Enter NBA Player Name:")
firstLabel = tk.Label(root, text="Sports Statistics")
space1 = tk.Label(root, text="")
entry = tk.Entry(root)
button = tk.Button(root, text="Show Player", command=show_player)
result = tk.Label(root, text="")
#nbaButton = tk.Button(root, text="NBA Statistics", command=show_player)
#nflButton = tk.Button(root, text="NFl Statistics", command=show_player)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # create widgets for main window
        self.label = tk.Label(self, text="Choose a league:")
        self.nbaButton = tk.Button(self, text="NBA", command=self.show_nba_screen)
        self.nflButton = tk.Button(self, text="NFL", command=self.show_nfl_screen)

        # pack widgets for main window
        self.label.pack()
        self.nbaButton.pack()
        self.nflButton.pack()

    def show_nba_screen(self):
        # create new window for NBA screen
        nba_window = tk.Toplevel(self)
        nba_window.title("NBA Statistics")
        
        # create widgets for NBA screen
        label = tk.Label(nba_window, text="Enter NBA player name:")
        entry = tk.Entry(nba_window)
        button = tk.Button(nba_window, text="Show Player")
        result = tk.Label(nba_window, text="")

        # pack widgets for NBA screen
        label.pack()
        entry.pack()
        button.pack()
        result.pack()

    def show_nfl_screen(self):
        # create new window for NFL screen
        nfl_window = tk.Toplevel(self)
        nfl_window.title("NFL Statistics")

        # create widgets for NFL screen
        label = tk.Label(nfl_window, text="Enter NFL player name:")
        entry = tk.Entry(nfl_window)
        button = tk.Button(nfl_window, text="Show Player")
        result = tk.Label(nfl_window, text="")

        # pack widgets for NFL screen
        label.pack()
        entry.pack()
        button.pack()
        result.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()


# Add widgets to the window
firstLabel.pack()
space1.pack()


label.pack()
entry.pack()
button.pack()
result.pack()

# Run the GUI
root.mainloop()

