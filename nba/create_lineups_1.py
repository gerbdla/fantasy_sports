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
    act_gt_proj_group = []
    final_player_group =[]
    act_gt_proj_group = get_team()
    
    #final_player_group.append(get_team('PG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('SG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('SF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('PF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('C',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
     
    workbook = xlsxwriter.Workbook('players_for_fanduel.xlsx')
    # high_proj_points = workbook.add_format()
    # high_proj_points.set_font_color('red')
    # high_proj_points.set_bold()
    # high_proj_points.set_bg_color('yellow')
    # high_proj_points.set_font_size(14)

    # highlight = workbook.add_format()
    # highlight.set_font_color('pink')
    # highlight.set_bold()
    # highlight.set_bg_color('yellow')
    # highlight.set_font_size(14)

    # starting = workbook.add_format()
    # starting.set_font_color('green')
    # starting.set_bold()
    # starting.set_bg_color('yellow')
    # starting.set_font_size(14)

    # high_pv = workbook.add_format()
    # high_pv.set_font_color('purple')
    # high_pv.set_bold()
    # high_pv.set_bg_color('yellow')
    # high_pv.set_font_size(14)

    worksheetPG = workbook.add_worksheet("ALL PLAYERS")
    #worksheetPG = workbook.add_worksheet("PG")
    #worksheetSG = workbook.add_worksheet("SG")
    #worksheetSF = workbook.add_worksheet("PF")
    #worksheetPF =  workbook.add_worksheet("SF")
    #worksheetC = workbook.add_worksheet("C")
    #worksheetALL = workbook.add_worksheet("All")
    #worksheetSTATS = workbook.add_worksheet("STATS")
    #worksheet_act_gt_proj = workbook.add_worksheet()
    
    # Set the column headers for spreadsheet
    col_count = 0
    act_gt_proj_headers = ["Name","Opp","Pos","PS","USG", \
    "PER","OPP_PACE","OPP_DEFF","LS_FGA","L5_FGA","S_FGA", \
    "Likes","Salary","Team","Opp", "L2_Min","L5_min","Floor_FP","Ceil_FP", \
    "Proj_Min","Proj_FP","Ceil_Floor"]    #('Nikola Jokic', '@POR', 'C', 114, '26', '31', 99, 111, 16, 15, 13, '', 11500, 'DEN', '@POR', 36, 32, 40.8, 61.0, 34.0, 53.5, 20.200000000000003)

    # Creat the column headers
    for name in act_gt_proj_headers:
        worksheetPG.write(0, col_count, name)
        col_count = col_count + 1
    # Inser the data into excel spreadsheet
    row_count = 1
    for field in get_team():
      col_count = 0      
      for column in field:
         worksheetPG.write(row_count, col_count  ,field[col_count])     
         col_count = col_count + 1    
      row_count = row_count + 1
    
    workbook.close()

if __name__ == '__main__':
    gpp()
