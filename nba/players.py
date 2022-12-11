#!/usr/bin/python
import pymysql
import csv
import pandas as pd
import re
import json
import requests
import xlsxwriter
import connection 
 
def get_team():
    db = connection.Connection.connect()
    cursor = db.cursor()
    sql = "call todays_players();"
    cur = cursor.execute(sql)
    all_players = cursor.fetchall()
    return all_players

def gpp():
    final_player_group = get_team()
    workbook = xlsxwriter.Workbook('players_for_fanduel.xlsx')
    
    starting = workbook.add_format()
    starting.set_font_color('green')
    starting.set_bold()
    starting.set_bg_color('yellow')
    starting.set_font_size(14)
    
    less_than_4999 = workbook.add_format()
    less_than_4999.set_font_color('red')
    less_than_4999.set_bold()
    less_than_4999.set_bg_color('yellow')
    less_than_4999.set_font_size(14)
    

    worksheetPG = workbook.add_worksheet("PG")
    
    # Set the column headers for spreadsheet
    col_count = 0
    headers = ["Name","Likes","Inj","Pos","Salary","Team","opp","rest","PS","USG", \
    "PER","OPP_PACE","OPP_DEFF","LS_FGA","L5_FGA","S_FGA", \
    "L2_Min","L5_min","Floor_FP","Ceil_FP", \
    "Proj_Min","Proj_FP","Ceil_Floor"]    

    # Creat the column headers
    for header in headers:
        worksheetPG.write(0, col_count, header)
        col_count = col_count + 1
        
    # Insert the data into excel spreadsheet
    row_count = 1
    # For each row in the dataset
    for row in final_player_group:
        if row[4] > 7000:
            col_count = 0
            for column in row:
              print(col_count)
              
              worksheetPG.write(row_count, col_count  ,row[col_count],less_than_4999)     
              col_count = col_count + 1   
        row_count = row_count + 1


    workbook.close()
    print("finished")

if __name__ == '__main__':
    gpp()
