from .wrapper import Resource
from flask import make_response, jsonify, request
from model import spectypes, missions
import json


class CalcStep(Resource):
    def get(self):
        result = []
        res = {'stepnum':0,'specs': json.loads(missions.mission.getMissionSpec())}
        result.append(res)
        return make_response(jsonify(result), 200)

    def post(self):
        p1 = request.json
        res = Calculator().calcNext(p1)
        return make_response(jsonify(res), 200)


class Calculator:
    def initParams(self):
        self.atm = 20
        self.voda = 20
        self.terr = 20
        self.spec1 = 10
        self.spec2 = 10
        self.spec3 = 10


    def calcNext(self, arr):
        self.initParams()
        for item in arr:
            self.applyStep(item)
        result = arr
        result[len(arr)-1]["specs"]["T0001"]["cnt"] = self.spec1
        result[len(arr)-1]["specs"]["T0002"]["cnt"] = self.spec2
        result[len(arr)-1]["specs"]["T0003"]["cnt"] = self.spec3

        result[len(arr) - 1]["params"] = {}
        result[len(arr) - 1]["params"]["E0001"] = self.atm
        result[len(arr) - 1]["params"]["E0002"] = self.voda
        result[len(arr) - 1]["params"]["E0003"] = self.terr

        return result


    def applyStep(self, item):
        # применяем ход
        self.countT0001(item["specs"]["T0001"]["muts"])
        self.countT0002(item["specs"]["T0002"]["muts"])
        self.countT0003(item["specs"]["T0003"]["muts"])

        item["specs"]["T0001"]["cnt"] = self.spec1
        item["specs"]["T0002"]["cnt"] = self.spec2
        item["specs"]["T0003"]["cnt"] = self.spec3

        item["params"] = {}
        item["params"]["E0001"] = self.atm
        item["params"]["E0002"] = self.voda
        item["params"]["E0003"] = self.terr


    #################################################################
    def countT0001(self, cnt):
        self.spec1 = self.spec1 + 1
        if self.spec1 > 15:
            self.spec1 = 5

        self.atm = self.atm - self.spec1
        self.terr = self.terr + self.spec1


    def countT0002(self, cnt):
        self.spec2 = self.spec2 + 2
        if self.spec2 > 20:
            self.spec2 = 3

        self.atm = self.atm + self.spec2
        self.terr = self.terr - round(self.spec2 * 0.5)



    def countT0003(self, cnt):
        self.spec3 = self.spec3 - 1
        self.voda = self.voda + self.spec3
