from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Comapnies = [
    {
        "Name": "Accenture",
        "Profile": "Python Developer",
        "Salary": 40.5
    }
]

class Jobs(Resource):
    def get(self, name):
        for company in Comapnies:
            if company["Name"] == name:
                return company
        return f"The company '{name}' dose not found!"

    def post(self, name):
        for company in Comapnies:
            if company["Name"] == name:
                return "{} already exist in the companies database!".format(name)
        
        input_data = request.get_json()
        company = {"Name": name, "Profile":input_data['Profile'], "Salary": input_data['Salary']}
        Comapnies.append(company)
        return company

    def put(self, name):
        request_data = request.get_json()
        
        for company in Comapnies:
            if company["Name"] == name:
                company.update(request_data)
                return company
                
        company = {"Name": name, "Profile": request_data['Profile'], "Salary": request_data['Salary']}
        Comapnies.append(company)
        return company

    def delete(self, name):
        for company in Comapnies:
            if company["Name"] == name:
                Comapnies.remove(company)
                return "Company '{}' is deleted!".format(name)

class Jobs_list(Resource):
    def get(self):
        return {'Comapnies': Comapnies}

api.add_resource(Jobs, "/comapny/<string:name>")
api.add_resource(Jobs_list, '/Comapnies/all_jobs')

if __name__ == "__main__":
    app.run(debug=True)