select  `Player Name`, Salary , `Opp Pace`, `Opp DEff`, `Opp DvP`,`Proj FP`,`Actual FP`,CAST(`Actual FP` AS SIGNED)- CAST(`Proj FP` AS SIGNED) AS FP_difference   from basketball.stats where `Actual FP` > 0  and `Proj FP` > 20    group by  `Player Name`, Salary , `Opp Pace`, `Opp DEff`, `Opp DvP`,`Proj FP`,`Actual FP`, FP_difference order by  `Player Name`,Salary , `Proj FP`,`Actual FP`  DESC ;