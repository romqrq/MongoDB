import pymongo
import os

from os import path
if path.exists("env.py"):
    import env

# ALL PYTHON CONSTANTS IN CAPITAL LETTERS AND SEPARATED BY UNDERSCORES
# using the OS lobrary to set a constant and using getenv() method to read in the environment
# variable that we set (in .bashrc)
MONGO_URI = os.getenv("MONGO_URI")
# MONGODB_NAME = os.environ.get('MONGODB_NAME')
# set another constant with the database name and another with collection name
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

# To INSERT A SINGLE new record:
# use insert_one or insert_many
# In this case, created a record as a dictionary with keys and values
# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'gender': 'm',
#            'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}
# #insert 'new_doc' into the collection
# coll.insert_one(new_doc)

# To INSERT MULTIPLE records
# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm',
#              'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'},
#              {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm',
#              'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]

# #Use insert_MANY method
# coll.insert_many(new_docs)

#To REMOVE specific data:
#USE delete_one() or delete_many()
# documents = coll.delete_one({'first': 'douglas'})

#To UPDATE a record
#use update_one or update_many
# coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'green'}})

# To print all the records
# documents = coll.find()

#To FIND specific data:
# documents = coll.find({'first': 'douglas'})
documents = coll.find({'nationality': 'american'})


for doc in documents:
    print(doc)
