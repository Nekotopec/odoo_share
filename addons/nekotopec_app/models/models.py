# -*- coding: utf-8 -*-

import secrets
from odoo import models, fields, api



# class nekotopec_app(models.Model):
#     _name = 'nekotopec_app.nekotopec_app'
#     _description = 'nekotopec_app.nekotopec_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class File(models.Model):
    _name = 'File'
    _description = 'Model of file.'

    file = fields.Binary()
    link = fields.Char(compute)