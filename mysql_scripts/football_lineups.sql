DROP TABLE IF EXISTS football.players;

CREATE TABLE football.players
SELECT *
from football.stats
where football.stats.`Proj Val` >= 1.4
and football.stats.Pos = 'WR'
and football.stats.`L3 Targets` > 4
and football.stats.`L3 FP` > 5
and football.stats.`Ceil FP` > 15
and football.stats.`Vegas Pts` >  20
and football.stats.`Yards Per Target` > 7.0
and football.stats.`S Targets` > 3;


INSERT INTO football.players 
SELECT *
from football.stats
where football.stats.`Proj Val` >=1.4
and football.stats.Pos = 'RB'
and football.stats.`S Rush Att` > 5
and football.stats.`L3 FP` > 10
and football.stats.`Ceil FP` > 14
and football.stats.`Vegas Pts` >  20
and football.stats.`Yards Per Rush Att` > 3
and football.stats.`Red Zone Targets` > 1.0;


INSERT INTO football.players
SELECT *
from football.stats
where football.stats.Pos = 'TE'
and football.stats.`L3 Targets` > 4
and football.stats.`L3 FP` > 5
and football.stats.`Ceil FP` > 15
and football.stats.`Vegas Pts` >  20
and football.stats.`Yards Per Target` > 6.0
and football.stats.`DvP` > 1
and football.stats.`S Targets` > 2.0;








