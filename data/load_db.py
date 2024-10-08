from data.db import get_db
import requests


def insert_data_if_empty(collection_name, api_url):
    client, db = get_db()
    collection = db[collection_name]
    if collection.find_one({}) == None:
        try:
            response = requests.get(api_url)
            data = response.json()
        except:
            print(f"Something went wrong with the server at {api_url}")
            return
        try:
            db[collection_name].insert_many(data)
        except:
            print(f"Something went wrong while loading the data into {collection_name} collection")
        finally:
            client.close()

BASE_URL = "http://jsonplaceholder.typicode.com/"

def insert_all_data_from_api_to_db_if_empty():
    insert_data_if_empty('users', f"{BASE_URL}users")
    insert_data_if_empty('posts', f"{BASE_URL}posts")