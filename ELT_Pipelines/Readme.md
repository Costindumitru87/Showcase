### **WHAT TO EXPECT:** ###

These pipelines are used to :
1. **Fetch the data from a public API**
     * used a header to pass on credentials
     * build the URL based on its components (based URL, endpoint, endpoint properties)
2. **Run light transformation of original JSON**
     * transform the JSON into a python native dictionary
     * iterate through dictionary elements and extract needed information
     * structure results and save as JSON
     * decorate results for BQ compatibility
3. **Used streaming inserts to load the data in BigQuery**
     * use developer credentials to authenticate for GCP access
     * use BQ python client to: 
     * get table schema
     * stream inserts into a staging area
4. **Run additional transformation for tabular formatting**
     * use built-in JSON functions to break down JSON into columns (Json extract scalar)
     * user-defined function for custom transformation 
5. **Expose data in a view that removes redundancy**
     * applies final data format casting      
6. **Additional pipelines steps that are not included**
     * integrity check on primary key violation 
     * data quality checks on selected elements, fields, columns
     * save data in mart table 


### USEFUL LINKS:
* [links Rapid API](https://rapidapi.com/marketplace)
* [Google Cloud Client Libraries](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html)
* [BQ streaming inserts documentation](https://cloud.google.com/bigquery/streaming-data-into-bigquery)


