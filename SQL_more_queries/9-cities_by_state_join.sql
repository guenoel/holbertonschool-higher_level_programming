-- select columns from different tables
SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s ON c.state_id = s.id;