-- La Mona China
SELECT tv_shows.title, tv_show_genres.id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.genre_id = tv_show_genres.id
ORDER BY tv_shows.title, tv_show_genres.id ASC;