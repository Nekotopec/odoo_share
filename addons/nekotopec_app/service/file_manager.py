import os
from tempfile import SpooledTemporaryFile
import logging
from odoo.http import request, HttpRequest
import odoo

request: HttpRequest = request

HOST = os.getenv('ODOO_HOST', 'localhost')
if HOST == 'localhost':
    PORT = ':8069'
else:
    PORT = None


def set_file(file_item: SpooledTemporaryFile) -> str:
    """Set temporary file to database and returns link."""
    file = {
        'file': file_item.read()
    }
    file_model = _get_file_model()
    created_file = file_model.create(vals_list=[file])
    return format_link(created_file.link)


def get_file(file_link: str) -> str:
    """Get binary file from database."""
    file_model = _get_file_model()
    binary_file = file_model.search([('link', '=', file_link)]).file
    return binary_file


def format_link(db_link: str) -> str:
    result_link = f'{HOST}{PORT}/nekotopec_share/file/download/{db_link}'
    logging.info(f'FILE_LINK:\t{result_link}')
    return result_link


def _get_file_model() -> odoo.models.Model:
    return request.env['nekotopec_app.file']
