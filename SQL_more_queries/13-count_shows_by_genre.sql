-- La Mona China
SELECT DISTINCT A.name AS genre, COUNT(A.id) AS number_of_shows
FROM tv_genres A
INNER JOIN tv_show_genres B
ON A.id = B.genre_id
GROUP BY A.name
ORDER BY number_of_shows DESC;