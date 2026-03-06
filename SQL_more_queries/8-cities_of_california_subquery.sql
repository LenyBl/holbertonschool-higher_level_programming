-- Write a SQL query to find all the cities in California. Use a subquery to find the state_id for California.
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');