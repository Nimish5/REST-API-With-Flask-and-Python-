# Udemy: REST API with Flask and Python
# Section 4: Video 71 & 72

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Ravi'
# app.config['JWT_AUTH_URL_RULE'] = '/signIn'
api = Api(app)

jwt = JWT(app, authenticate, identity)    # /auth

Peoples = [
    {
        "Name": "Neha Pathak Rajvaidya!",
        "Money": "All the money in the world!",
        "Luxury Item": "Home & Car",
        "Price": 100
    }
]

class Luxury(Resource):
    ravi = reqparse.RequestParser()
    ravi.add_argument("Money", type=str, required=True, help="This field is Mandatory!")
    ravi.add_argument("Luxury Item", type=str, required=True, help="This field is Mandatory!")
    ravi.add_argument("Price", type=int, required=True, help="This field is Mandatory!")

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['Name'] == name, Peoples), 'None')
        return {'Peoples': item}

    def post(self, name):
        if next(filter(lambda x: x['Name'] == name, Peoples), None):
            return f"The {name} already exist in the Peoples list!"

        input = Luxury.ravi.parse_args()

        item = {'Name': name, 'Money': input['Money'], 'Luxury Item': input['Luxury Item'], 
        'Price': input['Price']}
        Peoples.append(item)
        return item

    def put(self, name):
        # Luxury.ravi.add_argument('Place', type=str, required=True, help="Mandatory Field!")
        data = Luxury.ravi.parse_args()

        item = next(filter(lambda x: x["Name"] == name, Peoples), None)
        if item is None:
            item  = {'Name': name, 'Money': data['Money'], 'Luxury Item': data['Luxury Item'],
            'Price': data['Price']}
            Peoples.append(item)
            return item
        else:
            item.update(data)
            return item
        
    def delete(self, name):
        global Peoples
        Peoples = list(filter(lambda x: x['Name'] != name, Peoples))
        return "The item {} is deleted from the peoples list".format(name)

class All_Luxury(Resource):
    def get(self):
        return {'Peoples': Peoples}

api.add_resource(Luxury, "/people/<string:name>")
api.add_resource(All_Luxury, "/Peoples")

if __name__ == "__main__":
    app.run(debug=True)