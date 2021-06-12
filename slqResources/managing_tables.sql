### Create a new table with three columns
CREATE TABLE t (
    id INT PRIMARY KEY,
    name VARCHAR NOT NULL,
    price INT DEFAULT 0
);


#Create table backup
create or replace table t_backup as 
select * from t


### Delete the table from the database
DROP TABLE t ;


### Add a new column to the table
ALTER TABLE t ADD column;


### Drop column c from the table
ALTER TABLE t DROP COLUMN c ;


### ADD/DROP constraint
ALTER TABLE t ADD [DROP] constraint;


### Rename a table from t1 to t2
ALTER TABLE t1 RENAME TO t2;


### Rename column c1 to c2
ALTER TABLE t1 RENAME c1 TO c2 ;


### Remove all data in a table
TRUNCATE TABLE t;



