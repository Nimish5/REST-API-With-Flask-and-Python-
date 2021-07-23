# from flask import Flask
# from flask_restful import Resource, Api, reqparse

# app = Flask(__name__)
# api = Api(app)

# Friends = [
#     {
#         "Name": "Shubham Jain",
#         "Place": "Bhopal",
#         "Flexibility": 6.5
#     }
# ]

# class Add_frirends(Resource):
#     def get(self, name):
#         person = next(filter(lambda x: x['Name'] == name, Friends), 'None')
#         return {'A friend of mine': person}, 200 if person else 404

#     def post(self, name):
#         if next(filter(lambda x: x["Name"] == name, Friends), None):
#             return 'The {} already exist in the friends dictionary!'.format(name), 400

# # Know about reqparse/ RequestParser:  
# # https://flask-restplus.readthedocs.io/en/stable/parsing.html
# # https://flask-restful.readthedocs.io/en/latest/reqparse.html#:~:text=Flask%2DRESTful's%20request%20parsing%20interface,request%20object%20in%20Flask.
        
#         papa = reqparse.RequestParser()
#         papa.add_argument("Place",
#         type=str,
#         required=True, 
#         help='The field is mandatory!')
#         papa.add_argument('Flexibility')

#         data = papa.parse_args()

#         item = {"Name": name, "Place": data['Place'], "Flexibility": data['Flexibility']}
#         Friends.append(item)
#         return item, 201

#     def put(self, name):
#         parser = reqparse.RequestParser()
#         parser.add_argument('Place',
#         type=str,
#         required=True,
#         help='This field is required!')
#         parser.add_argument('Flexibility',
#         required=True,
#         help='This field is mandatory!')
#         parser.add_argument('Python Developer')
        
#         data = parser.parse_args()

#         item = next(filter(lambda x: x['Name'] == name, Friends), None)
#         if item is None:
#             item = {'Name': name, 'Place': data['Place'], "Flexibility": data['Flexibility'], 
#             "Python Developer": data['Python Developer']}
#             Friends.append(item)
#             return item
#         else:
#             item.update(data)
#             return item

#     def delete(self, name):
#         global Friends
#         Friends = list(filter(lambda x: x['Name'] != name, Friends))
#         return "The item {} is Deleted from the Friends list".format(name)


# class All_friends(Resource):
#     def get(self):
#         return {'Friends': Friends}

# api.add_resource(Add_frirends, "/friends/<string:name>")
# api.add_resource(All_friends, '/Friends')

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

Friends = [
    {
        "Name": "Nimish Pathak",
        "Work": "Looking out for a Job!",
        "Routine": "Tight schedule"
    }
]

class Add_friends(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Work', type=str, required=True, help='This field is mandatory!')
    parser.add_argument('Routine', type=str, required=True, help="This field can't be left blank!")

    def get(self, name):
        item = next(filter(lambda x: x['Name'] == name, Friends), 'None')
        return {"A friend of mine": item}, 200

    def post(self, name):
        if next(filter(lambda x: x["Name"] == name, Friends), None):
            return "The '{}' already exist in the Friends list".format(name)
        
        # Add_friends.parser.add_argument('Python Developer', type=str, required=True)

        input = Add_friends.parser.parse_args()
        item = {'Name': name, 'Work': input['Work'], 'Routine': input['Routine']}
        Friends.append(item)
        return item, 201

    def put(self, name):
        Add_friends.parser.add_argument('Favourite Animal', required=True, 
        help='This is a required field!')

        data = Add_friends.parser.parse_args()

        item = next(filter(lambda x: x['Name'] == name, Friends), None)
        if item is not None:
            item.update(data)
            return item
        else:
            item = {'Name': name, 'Work': data['Work'], 'Routine': data['Routine'], 
            'Favourite Animal': data['Favourite Animal']}
            Friends.append(item)
            return item

    def delete(self, name):
        global Friends
        Friends = list(filter(lambda x: x['Name'] != name, Friends))
        return f"The {name} is deleted from the items list!"

class All_friends(Resource):
    def get(self):
        return {'Friends': Friends}, 200

api.add_resource(Add_friends, '/My_friends/<string:name>')
api.add_resource(All_friends, '/Friends')

if __name__ == "__main__":
    app.run(debug=True)