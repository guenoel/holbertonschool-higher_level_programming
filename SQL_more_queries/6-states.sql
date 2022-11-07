-- create database, table, column with unique values
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT=1,
    name VARCHAR(256)
)