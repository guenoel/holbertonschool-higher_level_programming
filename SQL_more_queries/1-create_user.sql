-- create user
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
ALTER LOGIN user_0d_1 WITH PASSWORD = 'user_0d_1_pwd' OLD_PASSWORD = 'root';