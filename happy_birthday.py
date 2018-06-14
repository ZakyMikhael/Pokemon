
import requests
import hug
from flask import Flask
from falsk_restful import Api, Resource, reqparse


@hug.directive()
@hug.get()
@hug.local()
app = Flask(__name__)
api = Api(app)

Users = [
    {
        "name" : "Nicolas",
        "age" : 42,
    },
    {
        "name" : "Evil",
        "age" : 50,
    },
    {
        "name" : "Jass",
        "age" : 22,
    },
]

class user(Resource):
    def get (self, name):
        for user in Users:
            if (name == user ["name"]):
                return user, 200
        return "User not found", 404

        api.add_Resource (user, "/user/<string:name")
        app.run (debug=True)