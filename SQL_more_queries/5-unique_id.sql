-- create column with unique values
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 PRIMARY KEY,
    name VARCHAR(256)
)