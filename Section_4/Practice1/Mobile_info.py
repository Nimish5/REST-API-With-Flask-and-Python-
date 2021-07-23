from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from Authentication import authenticate, identity

app = Flask(__name__)
app.secret_key = "Nimish05"
api = Api(app)

jwt = JWT(app, authenticate, identity)    # /auth

Mobiles = [
    {
        "Name": "Neha Pathak Rajvaidya",
        "Mobile": "Iphone 11",
        "Company": "Apple", 
        "Price": 80000,
        "IMEI No.": "ADSDHBIIBB55"
    }
]

class Phone(Resource):
    nimish = reqparse.RequestParser()
    nimish.add_argument('Mobile', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Company', type=str, required=True, help='This field is mandatory!')
    nimish.add_argument('Price', type=int, required=True, help='This field is mandatory!')
    nimish.add_argument('IMEI No.', type=str, required=True, help='This field is mandatory!')
    
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["Name"] == name, Mobiles), 'None')
        return {"Mobile": item}, 200

    def post(self, name):
        if next(filter(lambda x: x['Name'] == name, Mobiles), None):
            return f"The {name} is already exist in the Mobiles list(in memory database)."
        
        input = Phone.nimish.parse_args()

        item = {'Name': name, 'Mobile': input['Mobile'], 'Company': input['Company'], 
        'Price': input['Price'], 'IMEI No.': input['IMEI No.']}
        
        Mobiles.append(item)
        return item, 201

    def put(self, name):
        data = Phone.nimish.parse_args()

        item = next(filter(lambda x: x['Name'] == name, Mobiles), None)
        if item:
            item.update(data)
            return item
        else:   # item is None
            item = {'Name': name, 'Mobile': data['Mobile'], 'Company': data['Company'], 'Price':
            data['Price'], 'IMEI No.': data['IMEI No.']}
            Mobiles.append(item)
            return item

    def delete(self, name):
        global Mobiles
        Mobiles = list(filter(lambda x: x['Name'] != name, Mobiles), None)
        return f"The {name} is deleted from the Mobiles list"

class Phone_List(Resource):
    def get(self):
        return {'Mobiles': Mobiles}


api.add_resource(Phone, "/mobile/<string:name>")
api.add_resource(Phone_List, "/Mobiles")
        

if __name__ == "__main__":
    app.run(debug=True)