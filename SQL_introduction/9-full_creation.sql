-- full creation
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
)
INSERT INTO hbtn_0c_0.second_table (
    id,
    name,
    score
)
VALUES
    (
        1,2,3,4
    ),
    (
        'John','Alex','Bob','George'
    ),
    (
        10,3,14,8
    );