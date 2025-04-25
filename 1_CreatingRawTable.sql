DROP TABLE IF EXISTS housing_raw;

CREATE TABLE housing_raw (
  longitude FLOAT,
  latitude FLOAT,
  housing_median_age FLOAT,
  total_rooms FLOAT,
  total_bedrooms FLOAT,
  population FLOAT,
  households FLOAT,
  median_income FLOAT,
  median_house_value FLOAT,
  ocean_proximity VARCHAR(50)
);

SELECT * FROM housing_raw;