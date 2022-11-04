-- list with conditions
SELECT score,name, IF(score>=10, "YES", "NO") FROM second_table ORDER BY score;