-- Write a SQL script that creates a database named hbtn_0d_usa and a table named states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Create a table named states with two columns: id and name.
-- The id column should be of type INT, have a default value of 0, and
-- should be the primary key. The name column should be of type VARCHAR(256).
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);