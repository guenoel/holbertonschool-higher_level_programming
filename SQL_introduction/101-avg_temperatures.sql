-- average temp per town
SELECT city,AVG(value) AS avg_temp FROM temperatures GROUP BY city;