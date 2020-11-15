# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request, HttpRequest

request: HttpRequest = request


class File(models.Model):
    _name = 'nekotopec_share.file'
    _description = 'Model of file.'

    filename = fields.Char()
    file = fields.Binary()
    link = fields.Char()
    host_link = fields.Char(compute='_compute_host_link', store=True)

    @api.depends('link')
    def _compute_host_link(self):
        for record in self:
            record.host_link = (f'{request.httprequest.host_url}'
                                f'nekotopec_share/file/download/{record.link}')
