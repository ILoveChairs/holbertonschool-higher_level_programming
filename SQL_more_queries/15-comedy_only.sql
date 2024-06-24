-- La Mona China
SELECT DISTINCT A.title
FROM tv_show_genres B
INNER JOIN tv_shows A ON A.id = B.show_id
INNER JOIN tv_genres C ON C.id = B.genre_id
WHERE C.name = 'Comedy'
ORDER BY A.title ASC;