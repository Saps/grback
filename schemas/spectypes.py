# -*- coding: utf-8 -*-
from marshmallow import Schema
from marshmallow import fields
from . import specmuts

class SSpecType(Schema):
    res_id = fields.String()
    title = fields.String()
    descr = fields.String()
    pic = fields.String()
    muts = fields.Nested(specmuts.SSpecMut, many=True)


