from .wrapper import Resource
from flask import make_response, jsonify

class SprMission(Resource):
    def get(self):
        result = {
            'title' : 'Спасение мира',
            'descr' : 'Надо просто прийти и спасти этот мир',
            'pic' : '/static/mpics/m0001.png'
        }
        return make_response(jsonify(message=result), 200)