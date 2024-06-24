-- Hail carrot
SELECT cities.id, cities.name, states.name
FROM cities A
LEFT JOIN countries B
ON A.country_id = B.id;