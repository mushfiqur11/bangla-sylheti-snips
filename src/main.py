import json
import pandas as pd
from auto_translate import translate_text
from nluData import SlotData
import db_utils
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def item():
    return 

if __name__ == "__main__":
    f = open('/home/muhammad/Research/nlu/data/benchmark_data.json')
    data = json.load(f)

    slotData = SlotData(data)
    
    # Set up the MongoDB connection
    mongo_client = db_utils.get_mongo_connection()

    if mongo_client:
        # Replace 'mydatabase' with the name of your database
        database_name = 'NLU'
        db = mongo_client[database_name]

        # Replace 'mycollection' with the name of your collection
        collection_name = 'data_gen'

        # Create a new collection
        collection = db_utils.create_collection(db, collection_name)

        if collection is not None:
            queries = slotData.get_queries()
            slotData.auto_query_translate(translator=translate_text, name='FormalBangla')
            slotData.auto_query_translate(name = 'InformalBangla')
            slotData.auto_query_translate(name = 'Sylheti')
            
            # Insert the sample items into the collection
            db_utils.insert_items(collection, queries)

    # Close the MongoDB connection
    if mongo_client:
        mongo_client.close()



# # slotData.auto_query_translate(translate_text)
# print(slotData.get_queries())
