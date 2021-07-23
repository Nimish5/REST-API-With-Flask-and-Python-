from flask_restful import Resource, reqparse
import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("sqldata.db")
        cursor = connection.cursor()

        query = "SELECT * FROM Users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user
        
class User_SignUp(Resource):      # To Register to new users in yhe database
    parser = reqparse.RequestParser()
    parser.add_argument("Username", type=str, required=True, help="Mandatory Field!")
    parser.add_argument("Password", type=str, required=True, help="Manadtory Field!")

    def post(self):
        payload = User_SignUp.parser.parse_args()

        if User.find_by_username(payload['Username']):
            return f"A user with the name '{payload['Username']}' already exists in the Users database!", 400
        
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()
 
        query = "INSERT INTO Users VALUES (NULL, ?, ?)"
        cursor.execute(query, (payload['Username'], payload['Password']))

        connection.commit()
        connection.close()

        return {'Message': 'User created/ Register sucessfully!'}

