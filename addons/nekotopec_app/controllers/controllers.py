# -*- coding: utf-8 -*-
import logging
import tempfile
import functools

import werkzeug
from odoo import http
from odoo.http import Response, HttpRequest, request, Response

from odoo.addons.nekotopec_app.service import file_manager

request: http.HttpRequest = request


def admin_rights_required(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        user_rec = request.env['res.users'].sudo().search(
            [('id', '=', request.session.uid)])
        if not user_rec.has_group('base.user_admin'):
            return werkzeug.exceptions.Forbidden()
        else:
            return func(*args, **kwargs)

    return wrapped


class FileController(http.Controller):
    @http.route('/nekotopec_app/nekotopec_app/', auth='admin')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/nekotopec_share/upload_form', auth='user')
    @admin_rights_required
    def upload_form(self, **kwargs):
        return Response(template='nekotopec_app.upload_file')
        # return http.request.render('nekotopec_app.upload_file')

    @http.route('/nekotopec_share/file/upload', auth='user')
    @admin_rights_required
    def upload_file(self, **kwargs):
        file_item: tempfile.SpooledTemporaryFile = kwargs.get('file')
        link = file_manager.set_file(file_item)
        return request.render('nekotopec_app.show_link', {'link': link})

    @http.route('/nekotopec_share/file/download/<file_id>', auth='public')
    def download_file(self, file_id, **kwargs):
        file = file_manager.get_file(file_id)
        if file is None:
            return Response(status=404)
        return file
