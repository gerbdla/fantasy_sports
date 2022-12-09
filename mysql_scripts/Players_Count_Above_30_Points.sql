

CREATE TABLE basketball.great_table SELECT `Player Name` as player_1, count(*) as count_1 from basketball.stats where `Actual FP` >  29 and `Proj FP` <  30  group by player_1 order by  count_1 DESC




