DELIMITER $$
CREATE DEFINER=`root`@`%` PROCEDURE basketball.`todays_players`()
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
basketball.players.Ceiling_Floor_Diff AS Ceiling_Floor,
basketball.salary_count.salary_count 
from 
basketball.players, basketball.salary_count
where basketball.players.Proj_FP > 25
and basketball.salary_count.Player_Name = basketball.players.Player_Name
order by Pos;
END$$
DELIMITER ;
