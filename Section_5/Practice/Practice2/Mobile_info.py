from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Authentication import authenticate, identity
from user import User_SignUp
from Mobiles_data import Phone, Phone_List

app = Flask(__name__)
app.secret_key = "Nimish05"
api = Api(app)

jwt = JWT(app, authenticate, identity)    # /auth


api.add_resource(Phone, "/mobile/<string:name>")
api.add_resource(Phone_List, "/Mobiles")
api.add_resource(User_SignUp, "/Register")

if __name__ == "__main__":
    app.run(debug=True)