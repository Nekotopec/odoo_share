# -*- coding: utf-8 -*-

import uuid
from odoo import models, fields, api


class File(models.Model):
    _name = 'nekotopec_app.file'
    _description = 'Model of file.'

    file = fields.Binary()
    link = fields.Char(compute="_make_link")

    def _make_link(self):
        for record in self:
            record.link = str(uuid.uuid4())
