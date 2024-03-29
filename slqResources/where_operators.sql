### Query rows using pattern matching (a% , %a, %a%, _a%, a_%, a__%, a%z)
SELECT c1, c2 
FROM mytable
WHERE c1 [NOT] LIKE a%;


### Query rows in a list
SELECT c1, c2 
FROM mytable
WHERE c1 [NOT] IN value_list;


### Query rows between two values
SELECT c1, c2 
FROM mytable
WHERE c1 BETWEEN 5 AND 100;


### Check if values in a table is NULL or not
SELECT c1, c2 
FROM mytable
WHERE c1 IS [NOT] NULL;
