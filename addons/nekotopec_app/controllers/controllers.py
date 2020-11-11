# -*- coding: utf-8 -*-
# from odoo import http


# class NekotopecApp(http.Controller):
#     @http.route('/nekotopec_app/nekotopec_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nekotopec_app/nekotopec_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nekotopec_app.listing', {
#             'root': '/nekotopec_app/nekotopec_app',
#             'objects': http.request.env['nekotopec_app.nekotopec_app'].search([]),
#         })

#     @http.route('/nekotopec_app/nekotopec_app/objects/<model("nekotopec_app.nekotopec_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nekotopec_app.object', {
#             'object': obj
#         })
