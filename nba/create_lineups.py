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

class LineupsWebsite:
    def source():
        return requests.get("https://www.lineups.com/nba/lineups").text

def teams_defense_by_position():
    db = DB_Connection.connect()
    cursor = db.cursor()
    sql = 'CALL `basketball`.`team_defense_position`();'
    cursor.execute(sql);
    results = cursor.fetchall()

def rem_dupes(dup_list):
    yooneeks = []
    for elem in dup_list:
        if elem not in yooneeks:
            yooneeks.append(elem)
    return yooneeks

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


#def best_three_players(best_three_positions):

    #submit three positions
    #select best player from each position
    #each team must be different
    
#def best_lowest_player():

    #find the best single player any position with the player_value

def find_over_under(team, money_lines):
    over_under = 0
    for line in money_lines:
        if (line["key"] == team and line["over_under"][1:] != "N/A"):
            over_under = float(line["over_under"][1:])
    return over_under

def find_spread(team, money_lines):
    for line in money_lines:
        if line["key"] == team:
            return line["spread"]
    return 0

def get_player_data(player_data, player_name):
    for player in player_data:
        if player["name"] ==  player_name:
            return player["rating"]
    return []

def player_data():
    # DG website is down
    # source = LineupsWebsite.source()
    # source = source.replace("<script nonce=\"STATE_TRANSFER_TOKEN\">window['TRANSFER_STATE'] = {}</script>", '')
    # dictionary = json.loads(re.search(r"window\['TRANSFER_STATE'\]\s=\s(\{.*\})<\/script>", source).group(1))
    # player_data = []
    # for team in dictionary['https://api.lineups.com/nba/fetch/lineups/gateway']['data']:
    #     for player in team["away_players"]:
    #         player_data.append(player)
    #     for player in team["home_players"]:
    #         player_data.append(player)
    return player_data

def money_lines():
    money_lines = []
    # DG Website is down
    # source = requests.get("https://www.lineups.com/nba/lineups").text
    # source = source.replace("<script nonce=\"STATE_TRANSFER_TOKEN\">window['TRANSFER_STATE'] = {}</script>", '')
    # dictionary = json.loads(re.search(r"window\['TRANSFER_STATE'\]\s=\s(\{.*\})<\/script>", source).group(1))
    # 
    # for team in dictionary['https://api.lineups.com/nba/fetch/lineups/gateway']['data']:
    #     money_lines.append(team["away_bets"])
    # for team in dictionary['https://api.lineups.com/nba/fetch/lineups/gateway']['data']:
    #     money_lines.append(team["home_bets"])
    return money_lines

def get_salary_count(player_name):
    db = DB_Connection.connect()
    cursor = db.cursor()
    sql = "SELECT salary_count from salary_count where Player_name = " + "'" + player_name + "'";
    cursor.execute(sql)
    results = cursor.fetchall()
    if results:
       return results[0][0]
    else:
        return 0

def get_money_line():
    vegas_data = []
    for team in money_lines():
        vegas_data.append(team["key"])
        vegas_data.append(team["spread"])
        vegas_data.append(float(team["over_under"][1:]))
    return vegas_data

def fanduel_player_name(player_name):
    players = []
    player = {}
    player['name'] = "Bradley Beal"
    player['new_name'] = "Brad Beal"
    players.append(player)
    for player in players:
        if player['name'] == player_name:
            return player['new_name']
        else:
            return player_name

def get_fanduel_player_data(player_name, starting_lineup):
    for player in starting_lineup:
        if player[0]  == player_name:
            return player
    return []

def is_starting(player_name, starting_lineup):
    for player in starting_lineup:
        if player[0]  == player_name:
            return 1
    return 0

def starting_lineups():
    # source = requests.get("https://www.lineups.com/nba/lineups").text
    # source = source.replace("<script nonce=\"STATE_TRANSFER_TOKEN\">window['TRANSFER_STATE'] = {}</script>", '')
    # dictionary = json.loads(re.search(r"window\['TRANSFER_STATE'\]\s=\s(\{.*\})<\/script>", source).group(1))
    starting_lineups = []
    # for player in dictionary['https://api.lineups.com/nba/fetch/lineups/gateway']['data']:
    #     for player in player['home_players']:
    #         lineup = {}
    #         lineup['player_name'] = fanduel_player_name(player['name'])
    #         lineup['rating'] = player['rating']
    #         lineup['fanduel_ownership'] = player['fanduel_ownership']
    #         lineup['position'] = player['position']
    #         lineup['rebounds'] = player['rebounds']
    #         lineup['fanduel_proj_points'] = player['fanduel_projection']
    #         lineup['assists'] = player['assists']
    #         starting_lineups.append(lineup)
    # 
    # for player in dictionary['https://api.lineups.com/nba/fetch/lineups/gateway']['data']:
    #     for player in player['away_players']:
    #         lineup = {}
    #         lineup['player_name'] = fanduel_player_name(player['name'])
    #         lineup['rating'] = player['rating']
    #         lineup['fanduel_ownership'] = player['fanduel_ownership']
    #         lineup['position'] = player['position']
    #         lineup['rebounds'] = player['rebounds']
    #         lineup['fanduel_proj_points'] = player['fanduel_projection']
    #         lineup['assists'] = player['assists']
    #         starting_lineups.append(lineup)
    return starting_lineups

def add_player_position_1(player, a_final_team_player1):
    position1 = {}
    position1["name"] =  player["name"]
    if float(player["ceiling_floor_diff"]) >= 20.1:
        position1["tier"] = "good_gpp"
    elif float(player["ceiling_floor_diff"])  <= 20:
        position1["tier"] = "good_cash_game"
    else:
        position1["tier"] = player["ceiling_floor_diff"]
    position1["salary"] =       player["salary"]
    position1["team"] =         player["team"]
    position1["opponent"] =     player["opponent"].replace("@", "")
    position1["pace"] =         player["opponent_pace"]
    position1["ou"] =           player["over_under"]
    position1["defense_efficiency"] = player["opponent_defense_efficiency"]
    position1["spread"] =       player["spread"]
    position1["rating"] =       player["rating"]
    position1["proj_points"] =  player["projected_fantasy_points"]
    position1["ceiling"] =      player["ceiling"]
    position1["cf_diff"] =      round(player["ceiling_floor_diff"])
    position1["position"] =     player["position"]
    #position1["salary_count"] = player["salary_count"]
    position1["ceiling_count"] =  player["ceiling_count"]
    position1["last_5_to_standard_min"] = player["last_5_to_standard_min"]
    position1["last_5_to_standard_points"] = player["last_5_to_standard_points"]
    position1["last_5_to_standard_fga"] = player["last_5_to_standard_fga"]
    position1["starting"] =  player["starting"]
    position1["Proj_Val"] = player["Proj_Val"]
    position1["200_to_205"] =  player["200_to_205"]
    position1["205_to_210"] =  player["205_to_210"]
    position1["210_to_215"] =  player["210_to_215"]
    position1["greater_than_215"] = player["greater_than_215"]
    position1["Rest"]             = player["Rest"]
    position1["fanduel_FP"] = player["fanduel_FP"]
    position1["PG"] = player["PG"]
    position1["SG"] = player["SG"]
    position1["SF"] = player["SF"]
    position1["PF"] = player["PF"]
    position1["C"] = player["C"]

    if player["projected_fantasy_points"] > 0:
        position1["salary/points"] = player["salary"] / player["projected_fantasy_points"]
    if player["projected_fantasy_points"] > 0:
        position1["salary/points"] = player["salary"] / player["projected_fantasy_points"]
    else:
        position1["salary/points"] = 0

    if not a_final_team_player1:
        a_final_team_player1.append(position1)
        position1 = {}
    else:
        if is_not_missing_player_1(position1, a_final_team_player1) == "true":
            x=0
        else:
            a_final_team_player1.append(position1)
            position1 = {}

    position1["210_to_215"] =       player[29]
    position1["greater_than_215"] = player[30]

def add_all_players(a_players, all_players):
    test = money_lines()
    the_player_data = player_data()
    count = 0
    starters = all_players
    for player in all_players:
        # unable to get starters data
        #fanduel_player = get_fanduel_player_data(player[0], starters)
        fanduel_player = get_fanduel_player_data(player[0], starters)
        for field in player:
            count = count + 1
            h_player = {}
            h_player["name"] = player[0]
            h_player["player_opponent"] = player[1]
            h_player["position"] = player[2]
            h_player["points_scored"] = player[3]
            h_player["usg"] = player[4]
            h_player["per"] = player[5]
            h_player["opponent_pace"] = player[6]
            h_player["opponent_defense_efficiency"] = player[7]
            h_player["last_two_fga"] = player[8]
            h_player["last_five_fga"] = player[9]
            h_player["s_fga"] =  player[10]
            h_player["likes"] =  player[11]
            h_player["salary"] = player[12]
            if player[13] == "NOR":
                h_player["team"] =  "NO"
            elif player[13] == "GSW":
                h_player["team"] =  "GS"
            elif player[13] == "SAS":
                h_player["team"] = "SA"
            elif player[13] == "NYK":
                h_player["team"] = "NY"
            else:
                h_player["team"] = player[13]
            h_player["opponent"] = player[14]
            h_player["last_two_minutes"] = player[15]
            h_player["last_five_minutes"] = player[16]
            h_player["floor_fantasy_points"] = player[17]
            h_player["ceiling"] = player[18]
            h_player["projected_minutes"] = player[19]
            h_player["projected_fantasy_points"] = player[20]
            if is_starting(player[0], starters):
                h_player["fanduel_FP"] = fanduel_player["fanduel_proj_points"]
            else:
                h_player["fanduel_FP"] = "NOT AVAILABLE"
            h_player["ceiling_floor_diff"] = player[21]
            h_player["starting"] = is_starting(player[0],starters)
            h_player["spread"] = find_spread(h_player["team"], test)
            h_player["over_under"] = find_over_under(h_player["team"], test)
            h_player["rating"] = get_player_data(the_player_data, player[0])
            h_player["salary_count"] = 555
            h_player["ceiling_count"] = 666
            if player[15] > 0 or player[16] > 0:
                h_player["last_5_to_standard_min"] = player[15]/player[16]
            else:
                h_player["last_5_to_standard_min"] = 0
            if player[22] > 0 or player[23] > 0:
                h_player["last_5_to_standard_points"] = player[22]/player[23]
            else:
                h_player["last_5_to_standard_points"] = 0
            if player[8] > 0 or player[9] > 0:
                h_player["last_5_to_standard_fga"] = player[8]/player[9]
            else:
                h_player["last_5_to_standard_fga"] = 0
            h_player["Proj_Val"]   = player[26]
            h_player["200_to_205"] = player[27]
            h_player["205_to_210"] = player[28]
            h_player["210_to_215"] = player[29]
            h_player["greater_than_215"] = player[30]
            h_player["Rest"] = player[31]

            h_player["PG"] = player[32]
            h_player["SG"] = player[33]
            h_player["SF"] = player[34]
            h_player["PF"] = player[35]
            h_player["C"] = player[36]
            a_players.append(h_player)
def get_team():
    return []
    
def get_team(position,high_spread,low_spread,min_ps,over_under,pace,ceiling,gpp=0):
    db = DB_Connection.connect()
    cursor = db.cursor()
    sql = "call todays_players();"
    cur = cursor.execute(sql)
    all_players = cursor.fetchall()
    a_players = []
    a_final_team_player1 = []
    a_final_team_player2 = []
    position1 = {}
    position2 = {}
    add_all_players(a_players, all_players)

    if gpp==1:
        for player in a_players:
            if  player["projected_fantasy_points"] >= min_ps \
            and player["starting"] == starting  \
            and player["over_under"] >= over_under \
            and player["ceiling"] > ceiling \
            and player["spread"] <= high_spread \
            and player["spread"] >= low_spread \
            and player["position"] == position:
                add_player_position_1(player, a_final_team_player1)
    elif gpp==0:
        for player in a_players:
            if  player["projected_fantasy_points"] >= min_ps \
            and player["starting"] == starting  \
            and player["over_under"] >= over_under \
            and player["ceiling"] > ceiling \
            and player["spread"] <= high_spread \
            and player["spread"] >= low_spread \
            and player["position"] == position:
                add_player_position_1(player, a_final_team_player1)
    elif gpp==2:
        for player in a_players:
            add_player_position_1(player, a_final_team_player1)

    df_single_level_cols = pd.DataFrame(a_final_team_player1)
    
    return a_final_team_player1


def is_not_missing_player_1(final_player,a_final_team):
    for player in a_final_team:
        if 'name' in player:
            if player["name"] == final_player["name"]:
                return "true"

def remove_dups(duplicate):
    return pd.DataFrame(duplicate).drop_duplicates().to_dict('records')

def players_with_high_proj_val():
    get_team_1()
    # final_player_group.append(get_team('PG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("point guards/high_total/low_spread:bench")
    # final_player_group.append(get_team('PG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("shooting guards/high_total/low_spread:starters")
    # final_player_group.append(get_team('SG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("shooting guards/high_total/low_spread:bench")
    # final_player_group.append(get_team('SG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("small forwards/high_total/low_spread:starters")
    # final_player_group.append(get_team('SF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("small forwards/high_total/low_spread:bench")
    # final_player_group.append(get_team('SF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("power forward/high_total/low_spread:starters")
    # final_player_group.append(get_team('PF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("power forward//high_total/low_spread:bench")
    # final_player_group.append(get_team('PF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("centers/high_total/low_spread:starters")
    # final_player_group.append(get_team('C',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    # print("centers/high_total/low_spread:bench")
    # final_player_group.append(get_team('C',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))

def gpp():
    ou = 200
    high_spread = 13
    low_spread = -13
    min_player_points = 10
    pace = 90
    gpp = 1
    final_player_group = []
    act_gt_proj_group = []
    ceiling = 25
    act_gt_proj_group = get_act_gt_proj()
      
    final_player_group.append(get_team('PG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    
    #final_player_group.append(get_team('PG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('SG',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('SF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('PF',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
    #final_player_group.append(get_team('C',high_spread,low_spread,min_player_points,ou,pace,ceiling,gpp))
     
    final_player_group = rem_dupes(final_player_group)
    workbook = xlsxwriter.Workbook('players_for_fanduel.xlsx')
    high_proj_points = workbook.add_format()
    high_proj_points.set_font_color('red')
    high_proj_points.set_bold()
    high_proj_points.set_bg_color('yellow')
    high_proj_points.set_font_size(14)

    highlight = workbook.add_format()
    highlight.set_font_color('pink')
    highlight.set_bold()
    highlight.set_bg_color('yellow')
    highlight.set_font_size(14)

    starting = workbook.add_format()
    starting.set_font_color('green')
    starting.set_bold()
    starting.set_bg_color('yellow')
    starting.set_font_size(14)

    high_pv = workbook.add_format()
    high_pv.set_font_color('purple')
    high_pv.set_bold()
    high_pv.set_bg_color('yellow')
    high_pv.set_font_size(14)

    worksheetPG = workbook.add_worksheet("PG")
    worksheetSG = workbook.add_worksheet("SG")
    worksheetSF = workbook.add_worksheet("PF")
    worksheetPF =  workbook.add_worksheet("SF")
    worksheetC = workbook.add_worksheet("C")
    worksheetALL = workbook.add_worksheet("All")
    worksheetSTATS = workbook.add_worksheet("STATS")
    worksheet_act_gt_proj = workbook.add_worksheet()


    headers = ["Name","Rest","Position","PG","SG","SF","PF","C","Salary","Team", \
    "Defense_Efficiency","OU","Spread","Rating","Proj_Points", \
    "FD_Proj_Points","fd_to_nerd_diff","Ceiling","CF_Diff", \
    "Salary/Points","Proj_Val","Starting",\
    "last_5_to_s_min","last_5_to_s_points",\
    "200_to_205", "205_to_210", "210_to_215", "Greater_than_215",\
    "act_gt_proj","good_player_count"]

    col_count = 0
    act_gt_proj_headers = ["Name","Opp","Pos","PS","USG", \
    "PER","OPP_PACE","OPP_DEFF","LS_FGA","L5_FGA","S_FGA", \
    "Likes","Salary","Team","Opp", "L2_Min","L5_min","Floor_FP", \
    "Ceil_FP","Proj_Min","Proj_FP","CF_DIFF"

    for name in act_gt_proj_headers:
        worksheet_act_gt_proj.write(0,col_count, name)
        col_count = col_count + 1

    row_count = 1

    for field in act_gt_proj_group:
        #print(field["name"]);
        worksheet_act_gt_proj.write(row_count, 0 ,field["name"])
        worksheet_act_gt_proj.write(row_count, 1 ,field["diff"])
        worksheet_act_gt_proj.write(row_count, 2 ,field["Proj_FP"])
        worksheet_act_gt_proj.write(row_count, 3 ,field["Actual_FP"])
        worksheet_act_gt_proj.write(row_count, 4 ,field["salary"])
        worksheet_act_gt_proj.write(row_count, 5 ,field["Rest"])
        worksheet_act_gt_proj.write(row_count, 6 ,field["Opp_Pace"])
        worksheet_act_gt_proj.write(row_count, 7 ,field["Opp_Deff"])
        worksheet_act_gt_proj.write(row_count, 8 ,field["USG"])
        row_count = row_count + 1


        col_count = 0
        for name in headers:
            worksheetPG.write(0,col_count, name)
            worksheetSG.write(0,col_count, name)
            worksheetPF.write(0,col_count, name)
            worksheetSF.write(0,col_count, name)
            worksheetC.write(0,col_count, name)
            col_count = col_count + 1
        col_count = 1

        row_count = 1
        good_player = 0
        Page1Count = 1
        Page2Count = 1
        Page3Count = 1
        Page4Count = 1
        Page5Count = 1


    for player in final_player_group:
        for field in player:
            if field["position"] == "PG" and field["starting"] == 1 \
            and field["proj_points"] > 20:
                worksheet_switch = 1
                worksheet = worksheetPG
                row_count = Page1Count
            elif field["position"] == "SG" and field["starting"] == 1 \
                and field["proj_points"] > 20:
            
                worksheet_switch = 1
                worksheet = worksheetSG
                row_count = Page2Count
            elif field["position"] == "SF" and field["starting"] == 1 \
            and field["proj_points"] > 20:

                worksheet_switch = 1
                worksheet = worksheetSF
                row_count = Page3Count
            elif field["position"] == "PF" and field["starting"] == 1:
                worksheet_switch = 1
                worksheet = worksheetPF
                row_count = Page4Count
            elif field["position"] == "C" and field["starting"] == 1 \
            and field["proj_points"] > 20:
                worksheet_switch = 1
                worksheet = worksheetC
                row_count = Page5Count
            else:
                worksheet = worksheetSTATS
                worksheet_switch = 0

            if worksheet_switch == 1:
                if field["Rest"] > 1:
                    worksheet.write(row_count,1, field["Rest"],highlight)
                else:
                    worksheet.write(row_count, 1 ,field["Rest"])

                worksheet.write(row_count, 2 ,field["position"])

                if (field["position"] == "PG"  and int(field["PG"][:2]) >= 49) \
                and field["starting"]== 1 and field["ou"] >= 220 and field["spread"] >= -6 \
                and field["spread"]<= 6:
                    worksheet.write(row_count, 3 , field["PG"][:2], highlight)
                else:
                    worksheet.write(row_count, 3 , field["PG"][:2])

                if (field["position"] == "SG"  and int(field["SG"][:2]) >= 49) \
                and field["starting"]== 1 and field["ou"] >= 220 and field["spread"] >= -6 \
                and field["spread"]<= 6:
                    worksheet.write(row_count, 4 , field["SG"][:2],highlight)
                else:
                    worksheet.write(row_count, 4 , field["SG"][:2])

                if (field["position"] == "SF"  and int(field["SF"][:2]) >= 39) \
                and field["starting"]== 1 and field["ou"] >= 220 and field["spread"] >= -6 \
                and field["spread"]<= 6:
                    worksheet.write(row_count, 5 , field["SF"][:2],highlight)
                else:
                    worksheet.write(row_count, 5 , field["SF"][:2])

                if (field["position"] == "PF"  and int(field["PF"][:2]) >= 39) \
                and field["starting"]== 1 and field["ou"] >= 220 and field["spread"] >= -6 \
                and field["spread"]<= 6:
                    worksheet.write(row_count, 6 , field["PF"][:2],highlight)
                else:
                    worksheet.write(row_count,  6, field["PF"][:2])

                if (field["position"] == "C"  and int(field["C"][:2]) > 39) \
                and field["starting"]== 1 and field["ou"] >= 220 and field["spread"] >= -6 \
                and field["spread"]<= 6:
                    worksheet.write(row_count, 7 , field["C"][:2],highlight)
                else:
                    worksheet.write(row_count, 7 , field["C"][:2])


                worksheet.write(row_count, 8 ,field["salary"])
                worksheet.write(row_count, 9 ,field["team"] + "-" + field["opponent"])
                worksheet.write(row_count, 10 ,field["defense_efficiency"])

                if field["ou"] >= 225:
                    worksheet.write(row_count,11,field["ou"],highlight)
                    good_player = good_player + 1
                else:
                    worksheet.write(row_count,11 ,field["ou"])

                if field["spread"] >= -10 and field["spread"] <= 10:
                    good_player = good_player + 1
                    worksheet.write(row_count, 12 ,field["spread"],highlight)
                else:
                    worksheet.write(row_count, 12 ,field["spread"])

                worksheet.write(row_count, 13 ,str(field["rating"]))

                if field["proj_points"] >= 40:
                    good_player = good_player + 1
                    worksheet.write(row_count, 14 ,field["proj_points"],highlight)
                elif field["proj_points"] >= 25 and field["proj_points"] <= 39:
                    worksheet.write(row_count, 14 ,field["proj_points"])
                else:
                    worksheet.write(row_count, 14 ,field["proj_points"])

                worksheet.write(row_count, 10 , field["fanduel_FP"])

                if field["fanduel_FP"] != "NOT AVAILABLE":
                    worksheet.write(row_count, 15, field["fanduel_FP"]/field["proj_points"])
                else:
                    worksheet.write(row_count, 15, "N/A")

                worksheet.write(row_count, 16 ,field["ceiling"])
                worksheet.write(row_count, 17 ,field["cf_diff"])

                if int(field["salary/points"]) <= 220:
                    worksheet.write(row_count, 18 , int(field["salary/points"]), highlight)
                else:
                    worksheet.write(row_count, 18 , int(field["salary/points"]), highlight)

                if field["Proj_Val"] >= 6:
                    worksheet.write(row_count, 19, field["Proj_Val"],highlight)
                else:
                    worksheet.write(row_count, 19 , field["Proj_Val"])

                if field["starting"] == 1:
                    good_player = good_player + 1
                    worksheet.write(row_count, 20 , "starting", highlight)
                else:
                    worksheet.write(row_count, 20 , "bench")

                if field["last_5_to_standard_min"] >= 1.4 and field["last_5_to_standard_points"] < 1:
                    worksheet.write(row_count, 21 , field["last_5_to_standard_min"], highlight)
                    worksheet.write(row_count, 22, field["last_5_to_standard_points"])

                elif field["last_5_to_standard_min"] >= 1 and field["last_5_to_standard_points"] >= 1:
                    good_player = good_player + 1
                    worksheet.write(row_count, 21 , field["last_5_to_standard_min"], highlight)
                    worksheet.write(row_count, 22, field["last_5_to_standard_points"], highlight)
                else:
                    worksheet.write(row_count, 21 , field["last_5_to_standard_min"])
                    worksheet.write(row_count, 22, field["last_5_to_standard_points"])

                test = field["200_to_205"]
                spread_field = 0

                if not (test is None):
                    try:
                        spread_field = int(field["200_to_205"][:2])
                    except:
                        spread_field = int(field["200_to_205"][:1])

                if field["ou"] >= 200 and field["ou"] <= 205:
                    worksheet.write(row_count, 23, field["200_to_205"], highlight)
                else:
                    worksheet.write(row_count, 23, field["200_to_205"])

                test = field["205_to_210"]
                spread_field = 0

                if not (test is None):
                    try:
                        spread_field = int(field["205_to_210"][:2])
                    except:
                        spread_field = int(field["205_to_210"][:1])

                if field["ou"] >= 205 and field["ou"] <= 210:
                    worksheet.write(row_count, 24,field["205_to_210"], highlight )
                else:
                    worksheet.write(row_count, 24, field["205_to_210"])

                test = field["210_to_215"]
                spread_field = 0

                if not (test is None):
                    try:
                        spread_field = int(field["210_to_215"][:2])
                    except:
                        spread_field = int(field["210_to_215"][:1])

                if field["ou"] >= 210 and field["ou"] <= 215:
                    worksheet.write(row_count, 25, field["210_to_215"], highlight)
                else:
                    worksheet.write(row_count, 25, field["210_to_215"])

                test = field["greater_than_215"]
                spread_field = 0

                if not (test is None):
                    try:
                        spread_field = int(field["greater_than_215"][:2])
                    except:
                        spread_field = int(field["greater_than_215"][:1])

                if field["ou"] > 215:
                    worksheet.write(row_count, 26, field["greater_than_215"], highlight)
                else:
                    worksheet.write(row_count, 26, field["greater_than_215"])

                worksheet.write(row_count, 27, field["opponent"])

                if good_player >= 4:
                    worksheet.write(row_count, 0 ,field["name"], highlight)
                else:
                    worksheet.write(row_count, 0 ,field["name"])

                the_count = 0

                for first_name in act_gt_proj_group:
                    if first_name["name"] == field["name"] and first_name["Actual_FP"] >= 20:
                        the_count = the_count + 1

                worksheet.write(row_count, 28, the_count)
                the_count = 0
                worksheet.write(row_count, 29 , good_player)


            if field["position"] == "PG":
                Page1Count = Page1Count + 1
            elif field["position"] == "SG":
                Page2Count = Page2Count + 1
            elif field["position"] == "SF":
                Page3Count = Page3Count + 1
            elif field["position"] == "PF":
                Page4Count = Page4Count + 1
            elif field["position"] == "C":
                Page5Count = Page5Count + 1

            else:
                row_count = row_count + 1

            good_player = 0
    workbook.close()

if __name__ == '__main__':
    gpp()
