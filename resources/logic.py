from .wrapper import Resource
from flask import make_response, jsonify, request
from model import spectypes, missions, specmuts
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
        self.atm = 1
        self.voda = 1
        self.terr = 1
        self.spec1 = 5
        self.spec2 = 5
        self.spec3 = 5
        self.stepnum = 0

        self.spec1muts = specmuts.specmut.get_specmuts_for_st("T0001")
        self.spec2muts = specmuts.specmut.get_specmuts_for_st("T0002")
        self.spec3muts = specmuts.specmut.get_specmuts_for_st("T0003")



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

        if "energy" not in result[len(arr) - 1]:
            result[len(arr) - 1]["energy"] = 0
        result[len(arr) - 1]["energy"] = result[len(arr) - 1]["energy"] + 40

        return result


    def applyStep(self, item):
        # применяем ход
        self.countT0001(item["specs"]["T0001"]["muts"])
        self.countT0002(item["specs"]["T0002"]["muts"])
        self.countT0003(item["specs"]["T0003"]["muts"])

        item["stepnum"] = self.stepnum
        self.stepnum = self.stepnum + 1

        item["specs"]["T0001"]["cnt"] = self.spec1
        item["specs"]["T0002"]["cnt"] = self.spec2
        item["specs"]["T0003"]["cnt"] = self.spec3

        self.atm = min(max(self.atm, 0),100)
        self.terr = min(max(self.terr, 0), 100)
        self.voda = min(max(self.voda, 0), 100)
        item["params"] = {}
        item["params"]["E0001"] = self.atm
        item["params"]["E0002"] = self.voda
        item["params"]["E0003"] = self.terr


    #################################################################
    # бабочки
    def countT0001(self, cnt):
        self.atm = self.atm + 1*self.spec1
        self.terr = self.terr + 2*self.spec1
        for mut in self.spec1muts:
            if mut.res_id in cnt:
                self.spec1 = self.spec1 + mut.pop
                self.atm = self.atm + mut.atm*self.spec1
                self.terr = self.terr + mut.terr*self.spec1
                self.voda = self.voda + mut.voda*self.spec1

    # крабы
    def countT0002(self, cnt):
        self.voda = self.voda + 2*self.spec2
        self.terr = self.terr + 1*self.spec2
        for mut in self.spec2muts:
            if mut.res_id in cnt:
                self.spec2 = self.spec2 + mut.pop
                self.atm = self.atm + mut.atm*self.spec2
                self.terr = self.terr + mut.terr*self.spec2
                self.voda = self.voda + mut.voda*self.spec2

    # водоросли
    def countT0003(self, cnt):
        self.atm = self.atm + 2*self.spec3
        self.voda = self.voda + self.spec3
        for mut in self.spec3muts:
            if mut.res_id in cnt:
                self.spec3 = self.spec3 + mut.pop
                self.atm = self.atm + mut.atm*self.spec3
                self.terr = self.terr + mut.terr*self.spec3
                self.voda = self.voda + mut.voda*self.spec3
