DROP TABLE basketball.`3000`;

CREATE TABLE basketball.`3000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 3500 and 4000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`4000`;

CREATE TABLE basketball.`4000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 4001 and 5000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`5000`;

CREATE TABLE basketball.`5000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 5001 and 6000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`6000`;

CREATE TABLE basketball.`6000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 6001 and 7000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`7000`;

CREATE TABLE basketball.`7000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 7001 and 8000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`8000`;

CREATE TABLE basketball.`8000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 8001 and 9000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`9000`;

CREATE TABLE basketball.`9000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 9001 and 10000
and Inj = 0
and `L5 FP` > `S FP`
and `Opp DvP` > -.05  
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`10000`;

CREATE TABLE basketball.`10000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 10001 and 11000
and Inj = 0
and `L5 FP` > `S FP`
order by  `Player Name` DESC;

DROP TABLE IF EXISTS basketball.`11000`;

CREATE TABLE basketball.`11000` SELECT `Player Name` , Team, Pos,Salary,`Opp DvP`, `Proj FP`
from basketball.stats 
where USG > 14 
and PER > 8
and PS >= 100
and `Proj Val` > 3.0
and `Ceil FP` >  25 
and  `L2 Min` >= `L5 Min`
and `Opp Pace` >= 100
and `L2 FGA` >= `L5 FGA`
and PS > 99
and Salary between 11001 and 12000
and Inj = 0
and `L5 FP` > `S FP`
order by  `Player Name` DESC;




