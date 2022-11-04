-- list with conditions
SELECT score,name, IF(score>=10) FROM second_table ORDER BY score DESC;