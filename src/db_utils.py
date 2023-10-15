import pymongo

def get_mongo_connection():
    try:
        # Replace 'localhost' with the address of your MongoDB server
        client = pymongo.MongoClient('mongodb+srv://muhammadankan:Bang1adesh@cluster0.vwjnph6.mongodb.net/')
        print("Connected to MongoDB successfully!")
        return client
    except pymongo.errors.ConnectionFailure:
        print("Failed to connect to MongoDB. Make sure MongoDB is running.")
        return None
    
def create_collection(database, collection_name):
    try:
        collection = database[collection_name]
        print(f"Collection '{collection_name}' created successfully.")
        return collection
    except Exception as e:
        print(f"Failed to create collection: {e}")
        return None

def insert_items(collection, items):
    try:
        # Insert multiple items at once using 'insert_many' method
        result = collection.insert_many(items)
        print(f"{len(result.inserted_ids)} items inserted successfully.")
    except Exception as e:
        print(f"Failed to insert items: {e}")