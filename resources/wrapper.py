from functools import wraps
from flask_restful import Resource
#as FRES
from flask import request, make_response, jsonify
from api import IAPI
import json
#from model import user

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(request.headers.environ)
        if not("HTTP_AUTHORIZATION" in request.headers.environ):
            return func(*args, **kwargs)##"No authorization"
        
        re = request.headers.environ['HTTP_AUTHORIZATION']
        rw = re.split(' ')
        if rw[0] != 'Bearer':
            return make_response(jsonify(message='No authorization'), 401)

        #us = user.user.checkSession(rw[1])
        if us == None :
            return make_response(jsonify(message='No session'), 401)
        #IAPI.US = us
        return func(*args, **kwargs)

        ##restful.abort(401)
    return wrapper


#class Resource(FRES):
    #method_decorators = [authenticate]

