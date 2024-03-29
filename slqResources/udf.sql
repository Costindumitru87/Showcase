### CREATE/REPLACE/ALTER/DROP User-Defined Function
CREATE FUNCTION [database_name]function_name (parameters)
RETURNS data_type AS
BEGIN
    SQL statements
    RETURN value
END;

ALTER FUNCTION [database_name]function_name (parameters)
RETURNS data_type AS
BEGIN
    SQL statements
    RETURN value
END;
    
DROP FUNCTION [database_name.]function_name;



### Transformation function example in BQ
create or replace function `test.NBA_transform.fn_teams`(data string)
returns struct <      
        data array<struct<
            city string,
            fullName string,
            teamId string,
            nickname string,
            logo string,
            shortName string,
            allStar string,
            nbaFranchise string,
            leagues struct<
                standard struct<
                    confName string,
                    divName string
          >
       >
    >
  >
>  

language js as """ return JSON.parse(data);""";


### Create view

create or replace view `test.NBA_transform.teams_raw` as
select `test.NBA_transform.fn_teams`(concat('''{"data":''',data,'''}''')).*  
from `test.NBA_import.teams_import`;

