from .wrapper import Resource
from flask import make_response, jsonify

class Info(Resource):
    def get(self, param_name):
        mess = "Hello, with %s param!" % param_name
        return make_response(jsonify(message=mess), 200)

    def get(self):
        mess = "Im working correct, nothing bad"
        return make_response(jsonify(message=mess), 200)

