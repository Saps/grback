# -*- coding: utf-8 -*-
from marshmallow import Schema
from marshmallow import fields

class SSpecMut(Schema):
    res_id = fields.String()
    spec_type_id = fields.String()
    name = fields.String()
    descr = fields.String()
    pic = fields.String()
    price = fields.Float()


