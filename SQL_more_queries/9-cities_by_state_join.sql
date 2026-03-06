-- Write a SQL query to find all the cities in California. Use a JOIN to connect the cities and states tables.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;