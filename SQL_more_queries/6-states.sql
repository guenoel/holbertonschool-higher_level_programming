-- create database, table, column with unique values
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT DEFAULT 1 PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256)
)