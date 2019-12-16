import pymongo
import os

from os import path
if path.exists("env.py"):
    import env

#ALL PYTHON CONSTANTS IN CAPITAL LETTERS AND SEPARATED BY UNDERSCORES
#using the OS lobrary to set a constant and using getenv() method to read in the environment
#variable that we set (in .bashrc)
MONGO_URI = os.getenv("MONGO_URI")
# MONGODB_NAME = os.environ.get('MONGODB_NAME')
#set another constant with the database name and another with collection name
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
    
conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)