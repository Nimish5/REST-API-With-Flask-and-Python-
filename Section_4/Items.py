from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Items = [
    {
        "Name": "Home",
        "Company": "S.S. Infinitus",
        "Price": 100.87
    }
]

class Products(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["Name"] == name, Items), 'None')
        return item, 200 if item else 404   # {"Item": item}
# 'next' keyword gives us the first item found/ matched by the filter function. 
# Instead of using list that gives us the list of items found/ matched by the filter function, its better to use 'next' as we are comparing only 1 item(name) from the list of Items.

    def post(self, name):
        if next(filter(lambda x: x['Name'] == name, Items), None):
            return f"The item,'{name}' already exist in the Items list!"

        # item = next(filter(lambda x: x['Name'] == name), 'None')
        # if item is not 'None':
        #     return f"An Item with '{name}' already exist in the database!"

        json_payload = request.get_json()
        item = {"Name": name, "Company": json_payload['Company'], "Price": json_payload['Price']}
        Items.append(item)
        return item

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['Name'] == name, Items), None)
        if item is not None:
            item.update(data)
            return item
        else:
            item = {"Name": name, "Company": data['Company'], "Price": data['Price']}
            Items.append(item)
            return item

    def delete(self, name):
        global Items
        Items = list(filter(lambda x: x["Name"] != name, Items))
        return {"Message":"Item is Deleted!"}          # "The item is Deleted!"


class Products_list(Resource):
    def get(self):
        return {'Items': Items}


api.add_resource(Products, '/item/<string:name>')
api.add_resource(Products_list, '/items')

if __name__ == "__main__":
    app.run(debug=True)
