# To SignUp/ Register a user directly into the database
# Video 80 & 81: Logging In and Reteiving Users from a database

import sqlite3
from flask_restful import Resource, reqparse 

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def search_by_username(cls, username):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def search_by_id(cls, _id):

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = "None"
        
        connection.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('Username', type=str, required=True, help='This field can not be left blank!')
    parser.add_argument('Password', type=str, required=True, help='This field can not be left blank!')

    def post(self):
        data = UserRegister.parser.parse_args()

# To check if the user already exist in the database, to avoid duplicacy. 
# OR To check that we are not registering a user with same username.
        if User.search_by_username(data['Username']):
            return f"A user with that username i.e. {data['Username']} already exist!"

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['Username'], data['Password']))

        connection.commit()
        connection.close()

        return {'Message': 'The User is Registered/ Created Sucessfully!'}

