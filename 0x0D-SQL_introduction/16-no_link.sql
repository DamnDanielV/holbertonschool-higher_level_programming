-- lists all records of the table second_table of hbtn_0c_0
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;