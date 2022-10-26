Classwork:
--SELECT * FROM north_american_cities where country ="Canada" order by population;
--select * from north_american_cities where country = "United States" order by Latitude DESC;
--SELECT * FROM north_american_cities where Longitude < -87.629798 order by Longitude ASC;
--SELECT * FROM north_american_cities where country = "Mexico" order by population DESC limit 2;
--SELECT city, population FROM north_american_cities where country = "United States" order by population DESC limit 2 offset 2;
HOMEWORK:
Lesson 6
--SELECT * FROM Movies inner join  Boxoffice on  Boxoffice.movie_id = Movies.id;
--SELECT * FROM Movies inner join  Boxoffice on  Boxoffice.movie_id = Movies.id where international_sales > domestic_sales;
-- SELECT * FROM Movies inner join  Boxoffice on  Boxoffice.movie_id = Movies.id order by rating  DESC;
Lesson 7
--SELECT DISTINCT building FROM employees;
--SELECT * FROM buildings;
--SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees ON building_name = employees.building;
Lesson 8
--SELECT name, role FROM employees where building is Null;
--SELECT DISTINCT building_name FROM buildings LEFT JOIN employees ON building_name = employees.building WHERE employees.building IS NULL;
Lesson 9
--SELECT DISTINCT title, (domestic_sales + international_sales) / 1000000 AS sales FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id;
--SELECT DISTINCT title, (rating * 10) AS rate_in_percent FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id;
--SELECT title FROM movies WHERE year % 2 = 0;
Lesson 10
--SELECT MAX(Years_employed) as gold_employee from Employees; 
--SELECT role, AVG(Years_employed) as avg_years_by_role from Employees Group by role;
--SELECT building, SUM(Years_employed) as avg_years_in_each_building from Employees Group by building;
Lesson 11
--SELECT Role, COUNT(*) AS Number_of_artists FROM Employees WHERE role = "Artist";
--SELECT Role, COUNT(*) AS Number_of_each_role FROM Employees group by role;
--SELECT  SUM(years_employed) AS Number_of_years FROM Employees where role = "Engineer";
Lesson 12
--SELECT director, count(title) as movies_directed from movies group by director;
--SELECT director, sum(domestic_sales + international_sales) as sales from movies left join boxoffice on boxoffice.movie_id = movies.id group by director;
Lesson 13
--Insert INTO movies VALUES (15, "Toy STory 4", "John Lasseter", 2022, 98);
--INSERT INTO Boxoffice VALUES (4, 8.7, 340000000, 270000000);
Lesson 14
--UPDATE Movies SET Director = "John Lasseter" WHERE title = "A Bug's Life";
--UPDATE Movies SET Year = 1999 WHERE Id = 3;
--UPDATE Movies SET Title = "Toy Story 3", Director = "Lee Unkrich" WHERE Id = 11;
Lesson 15
--DELETE FROM movies where year <2005;
--DELETE FROM movies where director = "Andrew Stanton";
Lesson 16
--CREATE TABLE Database (name INTEGER PRIMARY KEY, version FLOAT,director TEXT,Download_count INTEGER); 
Lesson 17 
--ALTER TABLE movies ADD column Aspect_ratio FLOAT
--ALTER TABLE movies ADD column Language TEXT DEFAULT English;
Lesson 18
--DROP TABLE IF EXISTS movies;
--DROP TABLE IF EXISTS boxoffice;