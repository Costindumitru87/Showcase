import requests
import simplejson as json
from google.cloud import bigquery
import datetime

headers = {
    'x-rapidapi-key': "63bd8ad080mshfd57e6b4647aexxxxxxxxxxxxxxxxxxx",
    'x-rapidapi-host': "flight-data4.p.rapidapi.com"
    }

url_airline = "https://flight-data4.p.rapidapi.com/get_airline_flights"
querystring_airline = {"airline":"UAE"}

response_json_airline = requests.request("GET", url_airline, headers=headers, params=querystring_airline).text
response_list_airline = json.loads(response_json_airline)

def get_airline_flights():
    flight_list = [] 
    for flights in response_list_airline:
        flight = flights.get("flight")
        flight_list.append(flight)
    return (flight_list)       
airline_flights_list = get_airline_flights()

def get_all_flights_info()->str:
    for flight_number in airline_flights_list:
        url_flight_info = "https://flight-data4.p.rapidapi.com/get_flight_info"
        querystring_flight_info ={"flight":flight_number}
        response_json_info = requests.request("GET", url_flight_info, headers=headers, params=querystring_flight_info).text
        response_list_info = json.loads(response_json_info)
        final_dict = response_list_info.get(flight_number)
        response_json_info = json.dumps(final_dict)  
 # instantiate the BQ client (open connection to BQ API, check and pass credentials, prepare BQ methods) 
        bq_client = bigquery.Client("test-costin")
 # declare destination table name
        table_name ="test-costin.Flights_import.airline_flights"                     
 # call BQ API to get table schema
        table_to_insert = bq_client.get_table(table_name)
        current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
 # wrap message to be inserted based on BQ require format
        rows_to_insert = [{"data":response_json_info,"loaded_at":current_timestamp}]
 # use insert_rows method given for iteration   
        bq_insert_job = bq_client.insert_rows(table_to_insert, rows_to_insert)
 # used print for debug purpose, empty list means no errors
        print(bq_insert_job)
      
get_all_flights_info()      

 #used Windows CommandPrompt and GCP account credentials to make the connection between them
 set GOOGLE_APPLICATION_CREDENTIALS=c:/Users/Costin/Desktop/VSC/nba_project/SA_Costin_dev.json
