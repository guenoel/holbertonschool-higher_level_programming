-- list with conditions
SELECT score,name FROM second_table IF(score>=10, "YES", "NO") ORDER BY score;