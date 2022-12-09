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
order by  `Player Name` DESC;
