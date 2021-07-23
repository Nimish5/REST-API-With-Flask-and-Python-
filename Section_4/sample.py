# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class Friends(Resource):
#     def get(self, name):
#         return {'Friend': name}

# api.add_resource(Friends, '/friend/<string:name>')

# if __name__ == "__main__":
#     app.run(debug=True)
# # app.run(debug=True)


# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class Company(Resource):
#     def get(self, name, id):
#         return f"Hello, I am {name} working in a good company having employee id {id}!"

# api.add_resource(Company, "/company/<string:name>/employee/<int:id>")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Family(Resource):
    def get(self, text, num):
        return "I {}, the number of people in my family are {}".format(text, num)

api.add_resource(Family, '/family/<string:text>/Nimish/<int:num>')

if __name__ == "__main__":
    app.run(debug=True)