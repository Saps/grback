# -*- coding: utf-8 -*-
from marshmallow import Schema
from marshmallow import fields

class SMission(Schema):
    res_id = fields.String()
    title = fields.String()
    description = fields.String()
    pic = fields.String()
    start_param = fields.String()
    start_specs = fields.String()


