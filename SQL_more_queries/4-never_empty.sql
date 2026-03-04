-- Create a table named id_not_null with two columns: id and name.
-- The id column should be of type INT and have a default value of 1. 
-- The name column should be of type VARCHAR(256) and should not allow NULL values.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);