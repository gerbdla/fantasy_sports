select basketball.players.Player_Name, basketball.players.Pos,
 players.Likes, 
 players.Salary, 
 players.Team, 
players.Opp, 
stats.Actual_FP AS stats_actual_fp,
players.Proj_FP AS Today_Proj_FP
from basketball.players, basketball.stats
where basketball.players.Player_Name = basketball.stats.Player_Name
order by Player_Name,Pos