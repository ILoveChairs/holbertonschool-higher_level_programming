-- La Mona China
SELECT DISTINCT A.title, C.name
FROM tv_shows A
LEFT JOIN tv_show_genres B ON A.id = B.show_id
LEFT JOIN tv_genres C ON C.id = B.genre_id
ORDER BY A.title, C.name ASC;