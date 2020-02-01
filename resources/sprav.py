from .wrapper import Resource
from flask import make_response, jsonify
from model import spectypes, missions

class SprMission(Resource):
    def get(self):
        result = missions.mission.getOne()
        return make_response(jsonify(message=result), 200)

class SprSpecType(Resource):
    def get(self):
        result = spectypes.spectype.getList()
        return make_response(jsonify(result), 200)