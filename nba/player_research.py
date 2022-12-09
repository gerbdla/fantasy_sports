#!/usr/bin/python
import pymysql
import csv
import pandas as pd
import re
import json
import requests

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'basketball'
db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
starting_home = []
starting_away = []

headers = ["Player_Name","Likes",
"Inj","Pos","Salary",
"Team","Opp","Rest",
"PS","USG","PER",
"Opp_Pace","Opp_Deff","Opp_Dvp",
"L2_FGA","L5_FGA","S_FGA",
"L2_Min","L5_Min","S_Min",
"L5_FP","S_FP","Floor_FP",
"Ceil_FP","Proj_Min","Proj_FP",
"Proj_Val","Actual_Min","Actual_FP",
"Actual_Val","Import_Date","Current_Date"]


def player_data():
    source = requests.get("https://www.lineups.com/nba/lineups").text
    dictionary = json.loads(re.search(r"window\['TRANSFER_STATE'\]\s=\s(\{.*\})<\/script>", source).group(1))
    player_data = []
    for team in dictionary['https://api.lineups.com/nba/fetch/lineups/gateway']['data']:
        for player in team["away_players"]:
            player_data.append(player)
        for player in team["home_players"]:
            player_data.append(player)
    return player_data


def research_player(player_name):
    db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    cursor = db.cursor()
    sql = "call Player_Data('" + player_name + "');"
    print(sql)
    cur = cursor.execute(sql)
    player_data = cursor.fetchall()
    file = open("player_data.csv", "w")
    file.write("Name, Opp, Pos, \
        PS, USG, PER \
        Opp_Pace, Opp_Deff, L2_FGA, \
        L5_FGA, Likes, Salary, \
        Team, Opp, L2_Min, L5_Min, \
        Floor_FP, Proj_Min, Proj_FP, \
        Ceiling_Floor_Diff, Salary_Count")
    file.write("\n")

    for player in player_data:
        for field in player:
            file.write(str(field))
            file.write(",")
            file.write("\n")

if __name__ == '__main__':
    research_player("John Wall")
