-- Use this query to set the missing values of total_bedrooms to the AVG of this column
UPDATE housing_raw
SET total_bedrooms = (SELECT AVG(total_bedrooms) FROM housing_raw)
WHERE total_bedrooms IS NULL;