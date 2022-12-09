DROP TABLE IF EXISTS basketball.`3000`;

CREATE TABLE basketball.`3000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`,
basketball.stats.`Ceil FP` - basketball.stats.`Floor FP` AS Ceiling_Floor_Diff
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.stats.Salary between 3500 and 4000
and basketball.current_game.`Player_Name` = basketball.stats.`Player Name`

order by  `Player_Name` DESC;

DROP TABLE IF EXISTS basketball.`4000`;

CREATE TABLE basketball.`4000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 4001 and 5000
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`5000`;

CREATE TABLE basketball.`5000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 3500 and 4000
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`6000`;

CREATE TABLE basketball.`6000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 6001 and 7000
order by  `Player_Name` DESC;

DROP TABLE IF EXISTS basketball.`7000`;

CREATE TABLE basketball.`7000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 7001 and 8000
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`8000`;

CREATE TABLE basketball.`8000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 8001 and 9000
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`9000`;

CREATE TABLE basketball.`9000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 9001 and 10000
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`10000`;

CREATE TABLE basketball.`10000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 10001 and 11000
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`11000`;

CREATE TABLE basketball.`11000` 
SELECT 
basketball.stats.`Player_Name` , 
basketball.stats.`Team`, 
basketball.stats.Pos,
basketball.stats.`Salary`,
basketball.stats.`Opp DvP`, 
basketball.stats.`Proj FP`
from basketball.stats, basketball.current_game
where basketball.stats.USG > 14 
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
and basketball.current_game.`Player Name` = basketball.stats.`Player Name`
and basketball.stats.Salary between 11001 and 12000
order by  `Player Name` DESC;




