-- Write a SQL query to return the name and score of all students in the second_table, ordered by score in descending order,
-- and excluding any records where the name is NULL.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;