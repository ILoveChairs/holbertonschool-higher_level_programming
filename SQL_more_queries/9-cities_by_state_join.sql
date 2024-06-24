-- Hail carrot
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.country_id = states.id;