from urllib import response
from algoliasearch.search_client import SearchClient
import json
from dotenv import load_dotenv
import os

load_dotenv('.env')

ALGO_APP_ID = os.environ['ALGO_APP_ID']
ALGO_API_KEY = os.environ['ALGO_API_KEY']
ALGO_INDEX_NAME = os.environ['ALGO_INDEX_NAME']


def client():
    client = SearchClient.create(ALGO_APP_ID, ALGO_API_KEY)
    index = client.init_index(ALGO_INDEX_NAME)
    return index




def partial_index_update_object(json_load):

    #will update objects and add if they dont exists


    index = client()
    response = index.partial_update_objects(json_load)
    return response  
 
def full_index_update_object(index,json_load):
    index = client()
    response = index.save_object(json_load)
    return response   


def get_index_object(json_load):
    index = client()
    response = index.get_object(1)

    return response   

def delete_index_object(json_load):
    index = client()
    response = index.delete_object(1)

    return response   



 

if __name__ == "__main__":


    json_load = {
        "objectID": "1", 
        "tags":["GFGFG"]
        }

    json_load_multi = [{'objectID': '1', "tag":2},
    {'objectID': '2', "tag":2}]
       
       
    #return_feed = partial_index_update_object(json_load_multi)
    #print(return_feed.raw_responses)
    """
    This will overwrite all records do not use unless you are builing direct feeds
    #return_feed = full_index_update(app_id,api_key,index,json_load)
    #print(return_feed.raw_responses)     
    """

    return_feed = get_index_object(1)
    print(return_feed.items())




    exit()

    
    #return_feed = delete_index_object(1)
    #print(return_feed.items())




