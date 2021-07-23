# Reteriving and Writing our Peoples Resources to a database 
# Udemy: Video 83, 84, 85 and 86

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Luxury(Resource):
    ravi = reqparse.RequestParser()
    ravi.add_argument("Money", type=str, required=True, help="This field is Mandatory!")
    ravi.add_argument("Luxury Item", type=str, required=True, help="This field is Mandatory!")
    ravi.add_argument("Price", type=int, required=True, help="This field is Mandatory!")

    @jwt_required()
    def get(self, name):
        item = self.search_by_name(name)
        if item:
            return item
        return {'Message': 'The people is not in the database!'}, 404
                                                            # @classmethod
    def search_by_name(self, name):                         #def search_by_name(cls, name):                              
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "SELECT * FROM Peoples WHERE Name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'Peoples': {'Name': name, 'Money': row[1], 'Luxury Item': row[2], 'Price': row[3]}}

    def post(self, name):
        if self.search_by_name(name):
            return {'Message': 'The person with this name {} already exist in the database'.format(name)}

        input = Luxury.ravi.parse_args()

        item = {'Name': name, 'Money': input['Money'], 'Luxury Item': input['Luxury Item'], 
        'Price': input['Price']}

        try:
            self.insert(item)         # A classmethod can also be called by using classname 
        except:
            return {'Messege': 'An error occured in inserting an item'}, 500

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "INSERT INTO Peoples VALUES (?, ?, ?, ?)"
        cursor.execute(query, (item['Name'], item['Money'], item['Luxury Item'], item['Price']))

        connection.commit()
        connection.close()
      
    def put(self, name):
        # Luxury.ravi.add_argument('Place', type=str, required=True, help="Mandatory Field!")
        data = Luxury.ravi.parse_args()

        item = self.search_by_name(name)
        People = {'Name': name, 'Money': data['Money'], 'Luxury Item': data['Luxury Item'], 
        'Price': data['Price']}

        if item is None:
            Luxury.insert(People)        # A classmethod can also be called by using classname
        else:
            self.update(People)

        return People

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "UPDATE Peoples SET Money=?, Luxury_Item=?, Price=? WHERE Name=?"
        cursor.execute(query, (item['Money'], item['Luxury Item'], item['Price'], item['Name']))
        # print(cursor.execute(query, (item['Money'], item['Luxury Item'], item['Price'], item['Name'])).rowcount)
        
        connection.commit()
        connection.close()
        
    def delete(self, name):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "DELETE FROM Peoples WHERE Name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'Messege': f'The item {name} is deleted from the Peoples database'}

class All_Luxury(Resource):
    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Peoples"
        result = cursor.execute(query)
        Peoples = []
        for row in result:
            Peoples.append({'Name': row[0], 'Money': row[1], 'Luxury Item': row[2], 'Price': row[3]})
        
        connection.close()

        return {'Peoples': Peoples}


# except:
# return "An Error occured in trying to inserting an Item", 500
# try:
# except:
# return {'Messege': 'An Error occured in updating an Item'}, 500 