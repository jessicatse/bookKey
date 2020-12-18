import pymongo
import datetime
import os
from dotenv import load_dotenv

## necessary for python-dotenv ##
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

mongo = "mongodb+srv://jtse:B0liaAtlas@cluster0.rsa9q.mongodb.net/bookKey?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo)

db = client['book_app']

users = db['users']
roles = db['roles']
books = db['books']
genres = db['genres']


def add_role(role_name):
    role_data = {
        'role_name': role_name
    }
    return roles.insert_one(role_data)


def add_genre(genre_name):
    genre_data = {
        'genre_name': genre_name
    }
    return genres.insert_one(genre_data)


def add_user(first_name, last_name, email, password, role):
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'role': role,
        'date_added': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }
    return users.insert_one(user_data)


def add_book(book_name, genre, author, publication_year, notes):
    book_data = {
        'book_name': book_name,
        'genre': genre,
        'author': author,
        'publication_year': publication_year,
        'notes': notes,
        'date_added': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }
    return books.insert_one(book_data)


def initial_database():
    # add roles
    admin = add_role('admin')
    contributor = add_role('contributor')
    user = add_role('user')

    # add users
    mike = add_user('Mike', 'Colbert', 'mike@mike.com', 'abc123', 'admin')

    # add genres
    sci_fi = add_genre('Science Fiction')
    romance = add_genre('Romance')
    classic = add_genre('Classic')
  

   
    # add book
    oldYeller = add_book('Old Yeller', 'Classic', 'CS Lewis','1870',  'read with tissues')      


def main():
    initial_database()
   

main()
