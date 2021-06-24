### what to expect ###

This pipelines are used to :
-- fetch the data from a public API
     used a header to pass on credetials
     build the url based on its components (based URL, endpoint, endpoint properties)
-- run light transformation of original Json
      transform the Json into a python native dictionary
      iterate through dictionary elements and extract neaded information
      structure results and save as Json
      decorate results for BQ compatibility
-- used streaming inserts to doad the data in BigQuery
      use developer credentials to authentificate for GCP access
      use BQ python client to: 
      get table schema
      stream inserts into staging area
 -- run additional transformation for tabelar formating
      use buit in Json functions to break down json inco columns (Json extract scalar)
      user defined function for custom transformation 
 -- expose data in view that
      removes redundency
      applies final data format casting
      

###  -- Additional pipelines stepts that are not included
--integrity check on primary key violatin 
--data quality check on selected elements, fields, columns
--save data in mart table 


### usefull links
--links Rapid API
-- https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html
BQ streaming inserts documentation
