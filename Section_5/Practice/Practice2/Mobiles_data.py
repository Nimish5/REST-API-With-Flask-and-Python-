from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Phone(Resource):
    nimish = reqparse.RequestParser()
    nimish.add_argument('Mobile', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Company', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Price', type=int, required=True, help='This field is mandatory!')
    nimish.add_argument('IMEI No.', type=str, required=True, help='This field is mandatory!')
    
    @jwt_required()
    def get(self, name):
        item = Phone.name_existance(name)         # self.name_existance(name)
        if item:
            return {'Mobile': item}
        return f"The {name} is not in the Mobiles database!", 404

    @classmethod
    def name_existance(cls, name):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Mobiles WHERE Name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return {'Name': name, 'Mobile': row[1], 'Company': row[2], 'Price': row[3],
            'IMEI NO.': row[4]}

    def post(self, name):
        if Phone.name_existance(name):
            return {'Message': f'The item with {name} is already exists in the Mobiles database!'}

        input = Phone.nimish.parse_args()

        item = {'Name': name, 'Mobile': input['Mobile'], 'Company': input['Company'], 'Price': 
        input['Price'], 'IMEI No.': input['IMEI No.']}

        try:
            self.storing(item)             # A classmethod can also be called by using classname
        except:
            {'Message': 'An error occured in storing an item.'}, 500
        
        return item, 201
        
    @classmethod
    def storing(cls, item):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "INSERT INTO Mobiles VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (item['Name'], item['Mobile'], item['Company'], item['Price'], item['IMEI No.']))

        connection.commit()
        connection.close()

    def put(self, name):
        data = Phone.nimish.parse_args()

        item = Phone.name_existance(name)
        Mobile = {'Name': name, 'Mobile': data['Mobile'], 'Company': data['Company'], 'Price':
        data['Price'], 'IMEI No.': data['IMEI No.']}

        if item:
            self.modify(Mobile)
        else:
            self.storing(Mobile)

        return Mobile, 201

    @classmethod
    def modify(cls, item):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "UPDATE Mobiles SET Mobile=?, Company=?, Price=?, IMEI_No=? WHERE Name=?"
        cursor.execute(query, (item['Mobile'], item['Company'], item['Price'], item['IMEI No.'], 
        item['Name']))

        connection.commit()
        connection.close()


    def delete(self, name):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "DELETE FROM Mobiles WHERE Name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'Message': f'An item {name} is deleted from the Mobiles database!'}

class Phone_List(Resource):
    def get(self):
        connection = sqlite3.connect('sqldata.db')
        cursor = connection.cursor()

        query = "SELECT * FROM Mobiles"
        result = cursor.execute(query)

        Mobiles = []
        for data in result:          # for row in result
            Mobiles.append({'Name': data[0], 'Mobile': data[1], 'Company': data[2], 'Price': data[3],
            'IMEI No.': data[4]})

        connection.close()

        return {'Mobiles': Mobiles}


