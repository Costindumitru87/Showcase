### Basic select
SELECT * 
FROM  mytable;


### Select columns
SELECT col1, col2
FROM mytable; 


### Query data and filter rows with a condition
SELECT c1, c2 
FROM mytable
WHERE condition;


### Query distinct rows from a table
SELECT DISTINCT c1
FROM mytable 
WHERE condition;


### Sort the result set in ascending or descending order
SELECT c1, c2 
FROM mytable
ORDER BY c1 ASC [DESC];


### Group rows using an aggregate function (AVG, COUNT, SUM, MAX, MIN)
SELECT c1, SUM(c2)
FROM mytable
GROUP BY c1;


### Filter groups using HAVING clause
SELECT c1, SUM(c2)
FROM mytable
GROUP BY c1
HAVING condition;
