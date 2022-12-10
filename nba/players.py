#!/usr/bin/python
import pymysql
import csv
import pandas as pd
import re
import json
import requests
import xlsxwriter


class DB_Connection:
    def connect():
        db_host = 'localhost'
        db_user = 'root'
        db_password = ''
        db_name = 'basketball'
        return pymysql.connect(db_host,db_user,db_password,db_name)

def get_act_gt_proj():
    act_gt_proj = {}
    arr_gt_proj = []
    db = DB_Connection.connect()
    cursor = db.cursor()
    cursor.execute("CALL `basketball`.`act_gt_proj`();")
    results = cursor.fetchall()

    for player in results:
        act_gt_proj["name"] = player[0]
        act_gt_proj["diff"] = player[1]
        act_gt_proj["Proj_FP"] = player[2]
        act_gt_proj["Actual_FP"] = player[3]
        act_gt_proj["salary"] = player[5]
        act_gt_proj["Rest"] = player[6]
        act_gt_proj["Opp_Pace"] = player[7]
        act_gt_proj["Opp_Deff"] = player[8]
        act_gt_proj["USG"] = player[9]
        arr_gt_proj.append(act_gt_proj)
        act_gt_proj = {}
    return arr_gt_proj

def get_team():
    db = DB_Connection.connect()
    cursor = db.cursor()
    sql = "call todays_players();"
    cur = cursor.execute(sql)
    all_players = cursor.fetchall()
    return all_players

def gpp():
    final_player_group = get_team()
     
    workbook = xlsxwriter.Workbook('players_for_fanduel.xlsx')
    
    # starting = workbook.add_format()
    # starting.set_font_color('green')
    # starting.set_bold()
    # starting.set_bg_color('yellow')
    # starting.set_font_size(14)

    worksheetPG = workbook.add_worksheet("ALL PLAYERS")
    
    # Set the column headers for spreadsheet
    col_count = 0
    headers = ["Name","Opp","Pos","PS","USG", \
    "PER","OPP_PACE","OPP_DEFF","LS_FGA","L5_FGA","S_FGA", \
    "Likes","Salary","Team","Opp", "L2_Min","L5_min","Floor_FP","Ceil_FP", \
    "Proj_Min","Proj_FP","Ceil_Floor"]    

    # Creat the column headers
    for name in headers:
        worksheetPG.write(0, col_count, name)
        col_count = col_count + 1
    # Inser the data into excel spreadsheet
    row_count = 1
    for field in final_player_group:
      col_count = 0      
      for column in field:
         worksheetPG.write(row_count, col_count  ,field[col_count])     
         col_count = col_count + 1    
      row_count = row_count + 1
    
    workbook.close()
    print("finished")

if __name__ == '__main__':
    gpp()
