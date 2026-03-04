-- Write a SQL script that creates a database named hbtn_0d_usa and a table named cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Create a table named cities with three columns: id, name, and state_id.
-- The id column should be of type INT, have a default value of 0, and
-- should be the primary key. The name column should be of type VARCHAR(256).
-- The state_id column should be of type INT and should be a foreign key that
-- references the id column of the states table.
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);