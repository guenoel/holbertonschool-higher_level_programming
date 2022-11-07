-- foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT,
    FOREIGN KEY (state_id) REFERENCES states(id)
)