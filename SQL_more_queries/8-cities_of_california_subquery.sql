-- asdfg
SELECT id INTO @california_id
    FROM states
    WHERE name = 'California';
SELECT *
    FROM cities
    WHERE state_id = @california_id
    ORDER BY id ASC;
