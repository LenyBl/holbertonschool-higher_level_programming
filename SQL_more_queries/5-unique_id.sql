-- Create a table named unique_id with two columns: id and name.
-- The id column should be of type INT, have a default value of 1, and
-- should be unique. The name column should be of type VARCHAR(256).
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);