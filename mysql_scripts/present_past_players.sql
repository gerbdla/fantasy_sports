DELIMITER $$
CREATE DEFINER=`root`@`%` PROCEDURE `todays_players`()
BEGIN
select basketball.players.Player_Name, 
basketball.players.Opp As player_opponent,
basketball.players.Pos,
basketball.players.PS,
basketball.players.USG,
basketball.players.PER,
basketball.players.Opp_Pace,
basketball.players.Opp_Deff,
basketball.players.L2_FGA,
basketball.players.L5_FGA,
basketball.players.S_FGA,
basketball.players.Likes, 
basketball.players.Salary, 
basketball.players.Team, 
basketball.players.Opp, 
basketball.players.L2_Min,
basketball.players.L5_Min,
basketball.players.Floor_FP,
basketball.players.Ceil_FP,
basketball.players.Proj_Min,
basketball.players.Proj_FP,
basketball.stats.Actual_FP,
basketball.players.Ceiling_Floor_Diff AS Ceiling_Floor
from 
basketball.players
where basketball.players.Player_Name = basketball.stats.Player_Name
and basketball.players.Player_Name = basketball.spreadsheet_sports.`Starting Lineup`
and basketball.players.Proj_FP > 25
order by Pos;
END$$
DELIMITER ;