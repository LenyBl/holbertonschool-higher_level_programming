-- Write a SQL query to count the number of students for each score in the second_table and
-- return the results ordered by score in descending order.
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;