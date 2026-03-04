-- Create a table named `first_table` with an auto-incrementing primary key `id` and a `name` column
CREATE TABLE IF NOT EXISTS first_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);