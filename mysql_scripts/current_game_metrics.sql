DROP TABLE IF EXISTS basketball.current_game_metrics;

CREATE TABLE basketball.current_game_metrics
SELECT 
basketball.current_game.`Player Name` ,  ]
basketball.current_game.likes,
basketball.current_game.`Team`, 
basketball.current_game.Pos,
basketball.current_game.`Salary`,
basketball.current_game.`Opp DvP`, 
basketball.current_game.`Proj FP`,
(basketball.current_game.`Ceil FP` - basketball.current_game.`Floor FP` ) AS Ceiling_Floor_Diff
from basketball.current_game
where basketball.current_game.USG > 14 
and basketball.stats.PER > 8
and basketball.stats.PS >= 100
and basketball.stats.`Proj Val` > 3.0
and basketball.stats.`Ceil FP` >  25 
and  basketball.stats.`L2 Min` >= basketball.stats.`L5 Min`
and  basketball.stats.`Opp Pace` >= 100
and basketball.stats.`L2 FGA` >= basketball.stats.`L5 FGA`
and basketball.stats.PS > 99
and basketball.stats.Inj = 0
and basketball.stats.`L5 FP` > basketball.stats.`S FP`
and basketball.stats.`Opp DvP` > -.05  
and basketball.
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 5001 and 6000
and (basketball.current_game.Inj = "o"
or basketball.current_game.Inj = "P"
or basketball.current_game.Inj <> "Q")
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.current_game.`Player Name` NOT IN (select `Player Name` 
from basketball.current_game where basketball.current_game.Inj = "O");




