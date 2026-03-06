-- Write a SQL query to find the genre_id of each show. The result should include
-- the show title and genre_id, and be ordered by show id in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;