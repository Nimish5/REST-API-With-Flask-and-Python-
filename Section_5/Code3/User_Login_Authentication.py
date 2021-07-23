# Udemy: REST API with Flask and Python
# Section 4: Video 71 & 72
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from Known_peoples import Luxury, All_Luxury

app = Flask(__name__)
app.secret_key = 'Ravi'
# app.config['JWT_AUTH_URL_RULE'] = '/signIn'
api = Api(app)

jwt = JWT(app, authenticate, identity)    # /auth

api.add_resource(Luxury, "/people/<string:name>")
api.add_resource(All_Luxury, "/Peoples")
api.add_resource(UserRegister, '/Register')

if __name__ == "__main__":
    app.run(debug=True)