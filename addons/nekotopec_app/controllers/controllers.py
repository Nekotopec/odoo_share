# -*- coding: utf-8 -*-
import functools
import logging

import werkzeug
from odoo import http
from odoo.addons.nekotopec_app.service import file_manager
from odoo.addons.web.controllers.main import content_disposition
from odoo.http import request, Response

request: http.HttpRequest = request


def admin_rights_required(func):
    """
    Decorator for routed Controller methods. Checks if user has admin rights.
    """

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
    @http.route('/nekotopec_share/upload_form', auth='user')
    @admin_rights_required
    def upload_form(self, **kwargs):
        return Response(template='nekotopec_app.upload_file')

    @http.route('/nekotopec_share/file/upload', auth='user')
    @admin_rights_required
    def upload_file(self, **kwargs):

        logging.info(type(kwargs.get('attachment')))
        file_item = kwargs.get('attachment')
        if not file_item:
            return werkzeug.exceptions.BadRequest()

        link = file_manager.set_file(file_item)
        return request.render('nekotopec_app.show_link', {'link': link})

    @http.route('/nekotopec_share/file/download/<file_id>', auth='public')
    def download_file(self, file_id, **kwargs):
        file = file_manager.get_file(file_id)
        if file is None:
            return request.not_found()
        return request.make_response(file.data,
                                     [('Content-Type',
                                       'application/octet-stream'),
                                      ('Content-Disposition',
                                       content_disposition(
                                           file.filename))])
