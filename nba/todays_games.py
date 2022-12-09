#!/usr/bin/python
import pymysql
import csv
from datetime import datetime
import sys

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'basketball'

db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)

def get_all_player_data():
    db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    cursor = db.cursor()
    db.cursor()
    cursor.execute("SELECT * from players")
    results = cursor.fetchall()

def populate_players_table(table1, table2):
    db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    cursor = db.cursor()
    sql = "DROP TABLE IF EXISTS " + table2
    cursor.execute(sql)
    sql = sql_create_players_table()
    cursor.execute(sql)
    print(sql);
    db.commit()
    #work
    sql = insert_data_into_players_table()
    cursor.execute(sql)
    # cursor.execute("CALL `basketball`.`team_defense_position`();")
    db.commit()
    # cursor.close()

def insert_previous_days_data():
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
    "Actual_Val"]

    with open('/Users/davidgerber/Downloads/previous_game.csv') as csv_data:
        my_reader= csv.reader(csv_data)
        db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
        cursor = db.cursor()
        result = []
        rownum = 0
        colnum = 0
        values = []
        joined_headers = ','.join(map(str, headers))
        next(my_reader)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for row in my_reader:
            row_values = []
            row_index = 0
            for field in headers:
                  row_values.append(row[row_index].replace("'","\\\'"))
                  row_index = row_index + 1
            row_values.append(current_time)
            test = ', '.join(["'%s'" % w for w in row_values])
            sql = "INSERT INTO basketball.stats \
                   (`Player_Name`, `Likes`, `Inj`, \
                    `Pos`, `Salary`, `Team`, \
                    `Opp`, `Rest`, `PS`, \
                    `USG`, `PER`, `Opp_Pace`, \
                    `Opp_DEff`, `Opp_DvP`, `L2_FGA`, \
                    `L5_FGA`, `S_FGA`, `L2_Min`, \
                    `L5_Min`,`S_Min`,`L5_FP`, \
                    `S_FP`, `Floor_FP`, `Ceil_FP`, \
                    `Proj_Min`, `Proj_FP`, `Proj_Val`, \
                    `Actual_Min`, `Actual_FP`,`Actual_Val`, \
                    `Import_Date`) \
                    VALUES (" + test + ");"
            print(sql)
            cursor.execute(sql)
            db.commit()

def create_and_populate_todays_slate_table(table_name):
    table_name = "todays_slate"
    headers = ["Player_Name"  ,
     "Likes","Inj", "Pos",
     "Salary", "Team","Opp",
     "Rest", "PS","USG"  ,
     "PER","Opp_Pace","Opp_DEff",
     "Opp_DvP", "L2_FGA","L5_FGA",
     "S_FGA"  ,"L2_Min"  ,"L5_Min",
     "S_Min"  ,"L5_FP","S_FP",
     "Floor_FP"  ,"Ceil_FP"  ,
     "Proj_Min"  ,"Proj_FP"  ,"Proj_Val"]

    with open('/Users/davidgerber/Downloads/current_game.csv') as csv_data:
        my_reader= csv.reader(csv_data)
        db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
        cursor = db.cursor()
        sql = "DROP TABLE IF EXISTS " + table_name
        cursor.execute(sql)
        db.commit()
        sql = sql_without_datatype(table_name)
        print("executing sql")
        cursor.execute(sql)
        result = []
        values = []
        joined_headers = ','.join(map(str, headers))
        next(my_reader)
        for row in my_reader:
            row_values = []
            row_index = 0
            for field in headers:
                    row_values.append(row[row_index].replace("'","\\\'"))
                    row_index = row_index + 1
                    values.append(row_values)
            test = ', '.join(["'%s'" % w for w in row_values])
            sql = "INSERT INTO todays_slate(Player_Name,Likes,Inj,Pos,Salary,Team,Opp,Rest,PS, \
            USG,PER,Opp_Pace,Opp_DEff,Opp_DvP,L2_FGA,L5_FGA,S_FGA,L2_Min,L5_Min,S_Min,L5_FP,S_FP, \
            Floor_FP,Ceil_FP,Proj_Min,Proj_FP,Proj_Val)VALUES(" + test + ");"
            print(sql)
            cursor.execute(sql)
            db.commit()


def sql_create_players_table():
    sql = "CREATE TABLE players (\
      Player_Name text,\
      Likes text,\
      Inj text,\
      Pos text, \
      Salary int(11) DEFAULT NULL,\
      Team text,\
      Opp text,\
      Rest int(11) DEFAULT NULL,\
      PS int(11) DEFAULT NULL,\
      USG text,\
      PER text,\
      Opp_Pace int(11) DEFAULT NULL, \
      Opp_DEff int(11) DEFAULT NULL,\
      Opp_DvP text,\
      L2_FGA int(11) DEFAULT NULL,\
      L5_FGA int(11) DEFAULT NULL,\
      S_FGA int(11) DEFAULT NULL,\
      L2_Min int(11) DEFAULT NULL,\
      L5_Min int(11) DEFAULT NULL,\
      S_Min int(11) DEFAULT NULL,\
      L5_FP double DEFAULT NULL,\
      S_FP double DEFAULT NULL,\
      Floor_FP double DEFAULT NULL,\
      Ceil_FP double DEFAULT NULL,\
      Proj_Min double DEFAULT NULL,\
      Proj_FP double DEFAULT NULL,\
      Proj_Val double DEFAULT NULL, \
      Ceiling_Floor_Diff double DEFAULT NULL, \
      200_to_205 varchar(50) DEFAULT NULL, \
      205_to_210 varchar(50) DEFAULT NULL, \
      210_to_215 varchar(50) DEFAULT NULL, \
      greater_than_215 varchar(50) DEFAULT NULL, \
      PG varchar(50) DEFAULT NULL, \
      SG varchar(50) DEFAULT NULL, \
      SF varchar(50) DEFAULT NULL, \
      PF varchar(50) DEFAULT NULL, \
      C varchar(50) DEFAULT NULL);"
    return sql

def sql_with_datatype(table_name):
    sql = "CREATE TABLE stats (Player_Name text,\
      Likes text,\
      Inj text,\
      Pos text, \
      Salary int(11) DEFAULT NULL,\
      Team text,\
      Opp text,\
      Rest int(11) DEFAULT NULL,\
      PS int(11) DEFAULT NULL,\
      USG text,\
      PER text,\
      Opp_Pace int(11) DEFAULT NULL, \
      Opp_DEff int(11) DEFAULT NULL,\
      Opp_DvP text,\
      L2_FGA int(11) DEFAULT NULL,\
      L5_FGA int(11) DEFAULT NULL,\
      S_FGA int(11) DEFAULT NULL,\
      L2_Min int(11) DEFAULT NULL,\
      L5_Min int(11) DEFAULT NULL,\
      S_Min int(11) DEFAULT NULL,\
      L5_FP double DEFAULT NULL,\
      S_FP double DEFAULT NULL,\
      Floor_FP double DEFAULT NULL,\
      Ceil_FP double DEFAULT NULL,\
      Proj_Min double DEFAULT NULL,\
      Proj_FP double DEFAULT NULL,\
      Proj_Val double DEFAULT NULL, \
      Ceiling_Floor_Diff double DEFAULT NULL \
      )"
    return sql

def create_negative_salary_count():
    db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    cursor = db.cursor()
    sql = "DROP TABLE IF EXISTS basketball.negative_salary_count ";
    cursor.execute(sql)
    sql = "CREATE TABLE basketball.negative_salary_count SELECT Player_Name,Salary,count(Salary) as negative_salary_count \
    from basketball.stats where Actual_FP < Proj_FP and USG > 15  \
    group by Salary, Player_Name;"
    cursor.execute(sql)

def create_count_tables():
    db = pymysql.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)
    cursor = db.cursor()
    sql = "DROP TABLE IF EXISTS basketball.salary_count ";
    cursor.execute(sql)
    db.commit()
    sql = "CREATE TABLE basketball.salary_count SELECT Player_Name, Team, Pos, \
    (Actual_FP - Proj_FP) as diff, Actual_FP, Proj_FP, Opp, Actual_Min, S_Min \
    from basketball.stats where Actual_FP > Proj_FP and USG > 15  \
    ;"
    cursor.execute(sql)
    db.commit()
    sql = "DROP TABLE IF EXISTS basketball.ceiling_count ";
    cursor.execute(sql)
    db.commit()
    sql = "CREATE TABLE basketball.ceiling_count SELECT Player_Name,count(Player_Name) AS count \
    from basketball.stats where Actual_FP > (Ceil_FP - 8) and USG > 15  \
    group by Player_Name;"
    cursor.execute(sql)
    db.commit()

def sql_without_datatype(table_name):
    sql = "CREATE TABLE " + table_name + "(Player_Name text,\
      Likes text, Inj text, Pos text, \
      Salary text, Team text, Opp text,\
      Rest text, PS text, USG text,\
      PER text, Opp_Pace text, Opp_DEff text,\
      Opp_DvP text, L2_FGA text, L5_FGA text,\
      S_FGA text, L2_Min text, L5_Min text,\
      S_Min text, L5_FP text, S_FP text,\
      Floor_FP text, Ceil_FP text, Proj_Min text,\
      Proj_FP text, Proj_Val text, Ceiling_Floor_Diff text)"
    return sql

def insert_data_into_players_table():
    
    
    # basketball.todays_slate.S_FP ,\
    # basketball.todays_slate.Floor_FP ,\
    # basketball.todays_slate.Ceil_FP ,\
    # basketball.todays_slate.Proj_Min ,\
    # basketball.todays_slate.Proj_FP ,\
    # basketball.todays_slate.Proj_Val, \
    # (basketball.todays_slate.Ceil_FP - basketball.todays_slate.Floor_FP ) AS Ceiling_Floor_Diff, \
    # 1 as 200_to_205,  \
    # 2 as 205_to_210,   \
    # 3 as 210_to_215,    \
    # 4 as greater_than_215, \
    # 5 as PG, \
    # 6 as SG, \
    # 7 as SF, \
    # 8 as PF, \
    # 9 as C \
    sql = "INSERT INTO basketball.players(Player_Name, Likes, Inj,Pos, Salary,Team, Opp, Rest, PS, USG, PER, \
    Opp_Pace,Opp_Deff,Opp_Dvp,L2_FGA,L5_FGA,S_FGA,L2_Min,L5_Min,S_Min,L5_FP,\
    S_FP,Floor_FP,Ceil_FP,Proj_Min,Proj_FP,Proj_Val,Ceiling_Floor_Diff,200_to_205,205_to_210,210_to_215,greater_than_215, \
    PG, SG, SF, PF,C) \
      SELECT  \
      basketball.todays_slate.Player_Name,\
      basketball.todays_slate.Likes, \
      basketball.todays_slate.Inj,\
      basketball.todays_slate.Pos, \
      basketball.todays_slate.Salary,\
      basketball.todays_slate.Team ,\
      basketball.todays_slate.Opp ,\
      basketball.todays_slate.Rest, \
      basketball.todays_slate.PS, \
      basketball.todays_slate.USG,\
      basketball.todays_slate.PER, \
      basketball.todays_slate.Opp_Pace, \
      basketball.todays_slate.Opp_Deff,\
      basketball.todays_slate.Opp_DvP, \
      basketball.todays_slate.L2_FGA, \
      basketball.todays_slate.L5_FGA ,\
      basketball.todays_slate.S_FGA, \
      basketball.todays_slate.L2_Min, \
      basketball.todays_slate.L5_Min ,\
      basketball.todays_slate.S_Min ,\
      basketball.todays_slate.L5_FP, \
      basketball.todays_slate.S_FP ,\
      basketball.todays_slate.Floor_FP ,\
      basketball.todays_slate.Ceil_FP ,\
      basketball.todays_slate.Proj_Min ,\
      basketball.todays_slate.Proj_FP ,\
      basketball.todays_slate.Proj_Val, \
      (basketball.todays_slate.Ceil_FP - basketball.todays_slate.Floor_FP ) AS Ceiling_Floor_Diff, \
      1 as 200_to_205, \
      2 as 205_to_210,   \
      3 as 210_to_215, \
      4 as greater_than_215, \
      5 as PG, \
      6 as SG, \
      7 as SF, \
      8 as PF, \
      9 as C \
      from basketball.todays_slate \
      where basketball.todays_slate.Player_Name NOT IN (select Player_Name from basketball.todays_slate \
      where basketball.todays_slate.Inj = 'O');"
    
    return sql

if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    #print('Argument List:', str(sys.argv))
    #print(str(sys.argv[1]))
    if str(sys.argv[1]) == "previous":
        insert_previous_days_data()
    else:
        print("else")
        create_count_tables()
        create_and_populate_todays_slate_table("basketball.todays_slate")
        populate_players_table("basketball.todays_slate","basketball.players")
