import requests
import simplejson as json
from google.cloud import bigquery
import datetime

headers = {
    'x-rapidapi-key': "63bd8ad080mshfd57e6b4647aeddpxxxxxxxxxxxxx",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

entity = "standings"

base_url ="https://api-nba-v1.p.rapidapi.com/"
endpoints ={}
endpoints["games2018"] = "games/seasonYear/2018"
endpoints["players"] = "players/league/standard"
endpoints["teams"] = "teams/league/standard"
endpoints["standings"] = "standings/standard/2018"

def build_url(endpoint)->str:
    url = f"{base_url}{endpoints.get(endpoint)}"
    return url

created_url = build_url(entity)

response_json = requests.request("GET", created_url, headers=headers).text
respone_json_dict = json.loads(response_json)
response_list = respone_json_dict.get("api").get(entity)
response_json = json.dumps(response_list)
    

bq_client = bigquery.Client("test-costin")
table_name = f"test-costin.NBA_import_test.{entity}"                     
table_to_insert = bq_client.get_table(table_name)
current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
rows_to_insert = [{"data":response_json,"loaded_at":current_timestamp}]   
bq_insert_job = bq_client.insert_rows(table_to_insert, rows_to_insert)
