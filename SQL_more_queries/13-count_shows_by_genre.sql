-- Write a SQL query to count the number of shows for each genre. The result should
-- include the genre name and the number of shows, and be ordered by the number of
-- shows in descending order.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;