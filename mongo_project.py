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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Creating SHOW MENU function


def show_menu():
    print('')
    print('1. Add a record')
    print('2. Find a record by name')
    print('3. Edit a record')
    print('4. Delete a record')
    print('5. Exit')

    option = input('Enter option: ')
    return option

# Helper function to assist with our find, edit and delete functions


def get_record():
    first = input('Enter first name > ')
    last = input('Enter last name > ')

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print('Error accessing the database')

    if not doc:
        print('')
        print('Error! No results found')

    return doc


def add_record():
    print('')
    first = input('Enter first name > ')
    last = input('Enter last name > ')
    dob = input('Enter date of birth > ')
    gender = input('Enter gender > ')
    hair_colour = input('Enter hair colour > ')
    occupation = input('Enter occupation > ')
    nationality = input('Enter nationality > ')

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender.lower(
    ), 'hair_colour': hair_colour.lower(), 'occupation': occupation.lower(), 'nationality': nationality.lower()}

    try:
        coll.insert_one(new_doc)
        print('')
        print('Document inserted')
    except:
        # This is to catch any errors. In real world we want to be more specific, drill down on these possible
        # errors and act on them proactively
        print('Error accessing the database')

# Finds records


def find_record():
    # here doc uses the helper function get_record() to avoid repetition.
    doc = get_record()
    if doc:
        print('')
        # Using a for loop to iterate through the keys and values of the result
        # The .ITEMS() method steps through each individual value in our dictionary
        for k, v in doc.items():
            if k != '_id':
                print(k.capitalize() + ': ' + v.capitalize())


# EDIT record funcion
def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print('')
        for k, v in doc.items():
            if k != '_id':
                # The formatting for the V here is like that to show it inside brackets so we know what
                # is the actual value
                update_doc[k] = input(k.capitalize() + ' [' + v + '] > ')

                if update_doc[k] == '':
                    update_doc[k] = v
        try:
            coll.update_one(doc, {'$set': update_doc})
            print('')
            print('Document updated')
        except:
            print('Error accessing the database')


def delete_record():

    doc = get_record()

    if doc:
        print('')
        #Here we iterate through each of the values so we are sure we're deleting the right document and
        #asking for confirmation
        for k, v in doc.items():
            if k != '_id':
                print(k.capitalize() + ': ' + v.capitalize())

        print('')
        #This confirmation variable stores the result of the input statement and prompt a text confirming
        #that is the desired action the user wants to take.
        confirmation = input('Is this the document you want to delete?\nY or N > ')
        print('')

        if confirmation.lower() == 'y':
            try: 
                coll.delete_one(doc)
                print('Document deleted!')
            except:
                print('Error accessing the database')
        else:
            print('Document not deleted')
            


# Defining the main loop.
# This will continue to call the menu everytime we come back to it
def main_loop():
    # with the while True, the loop is gonna run forever
    while True:
        option = show_menu()
        if option == '1':
            # print('You have selected option 1')
            add_record()
        elif option == '2':
            # print('You have selected option 2')
            find_record()
        elif option == '3':
            # print('You have selected option 3')
            edit_record()
        elif option == '4':
            # print('You have selected option 4')
            delete_record()
        elif option == '5':
            conn.close()
            break
        else:
            print('Invalid option')
        print('')


# Calls the connection
conn = mongo_connect(MONGO_URI)
# Creates the collection
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
