-- Quick comment\n
SELECT 
    DISTINCT score, 
    COUNT(*) AS "Count"
    FROM second_table
    GROUP BY score
    ORDER BY score DESC;
