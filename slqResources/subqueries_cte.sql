### Subquery in a SELECT clause example
SELECT 
	l.name AS league,
    ROUND(AVG(m.home_goal + m.away_goal), 2) AS avg_goals,
    -- Selecting and rounding the average total goals for the season
    (SELECT ROUND(AVG(home_goal + away_goal), 2) 
     FROM match
     WHERE season = '2013/2014') AS overall_avg
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
WHERE season = '2013/2014'
GROUP BY l.name;


### Joining Subqueries in a FROM clause example
SELECT
    c.name AS country_name,
    COUNT(sub.id) AS matches
FROM country AS c
-- Inner joining  the subquery onto country
INNER JOIN (SELECT country_id, id 
           FROM match
           -- Filtering the subquery by matches with 10+ goals
           WHERE (home_goal + away_goal) >= 10) AS sub
ON c.id = sub.country_id
GROUP BY country_name;



### Subquery in a WHERE clause example
SELECT 
  date,
	home_goal,
	away_goal
FROM  matches_2013_2014
-- Filter for matches where total goals exceeds 3x the average
WHERE (home_goal + away_goal) > 
       (SELECT 3 * AVG(home_goal + away_goal)
        FROM matches_2013_2014);
        
        
### Declaring a CTE example
WITH match_list AS (
    SELECT 
  	country_id, 
  	id
    FROM match
    WHERE (home_goal + away_goal) >= 10)
SELECT
    l.name AS league,
    COUNT(match_list.id) AS matches
FROM league AS l
-- Joining the CTE to the league table
LEFT JOIN match_list ON l.id = match_list.country_id
GROUP BY l.name;
        
        







