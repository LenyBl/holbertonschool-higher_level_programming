-- Write a SQL query to find the top score from the second_table and return all the records with that score.
SELECT (score, name) FROM second_table WHERE score = (SELECT MAX(score) FROM second_table);