from re import A
from urllib import response
from algoliasearch.search_client import SearchClient
import json
from dotenv import load_dotenv
import os
import csv
import json
import pandas as pd
import sys

load_dotenv('.env')

ALGO_APP_ID = os.environ['ALGO_APP_ID']
ALGO_API_KEY = os.environ['ALGO_API_KEY']
ALGO_INDEX_NAME = os.environ['ALGO_INDEX_NAME']

def client():
    try:
        client = SearchClient.create(ALGO_APP_ID, ALGO_API_KEY)
        index = client.init_index(ALGO_INDEX_NAME)
        return index
    except Exception as e:
        print('issue at client() function, error', e)
        sys.exit(1)

def csv_to_json(filename):
    try:
        result = []
        df = pd.read_csv('algo_push_objects.csv')
        for objectID, objectdf in df.groupby('objectID'):
            object_dict = {'objectID': objectID}
            for index, row in objectdf.iterrows():
                if row['datatype'] == 'boolean':
                    object_dict[row['object']] =  bool(row['value'] == 'true')
                else:
                    object_dict[row['object']] = row['value']
            result.append(object_dict)
        final_result = pd.read_json(json.dumps(result)).to_dict('records')
        return final_result
    except Exception as e:
        print('issue with csv input feed,  error',e)
        sys.exit(1)




def partial_index_update(json_load):
    index = client()
    try:
        response = index.partial_update_objects(json_load)
        return response  
    except Exception as e:
        print('issue with json input, error = ',e)
        sys.exit(1)
 






if __name__ == "__main__":

    #input_feed
    final_result = csv_to_json('algo_push_objects.csv')
  

    #tags_update
    return_feed = partial_index_update(final_result)

    print('Success Feed')
    sys.exit(0)
    

