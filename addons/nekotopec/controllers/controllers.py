# -*- coding: utf-8 -*-
# from odoo import http


# class Nekotopec(http.Controller):
#     @http.route('/nekotopec/nekotopec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nekotopec/nekotopec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nekotopec.listing', {
#             'root': '/nekotopec/nekotopec',
#             'objects': http.request.env['nekotopec.nekotopec'].search([]),
#         })

#     @http.route('/nekotopec/nekotopec/objects/<model("nekotopec.nekotopec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nekotopec.object', {
#             'object': obj
#         })
