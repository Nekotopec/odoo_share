import base64
import logging
import uuid
from typing import NamedTuple, Union

import odoo
from odoo.http import request, HttpRequest
from werkzeug.datastructures import FileStorage

request: HttpRequest = request


class File(NamedTuple):
    data: bytes
    filename: str
    link: str = None


def set_file(file_item: FileStorage) -> str:
    """Set temporary file to database and returns link."""

    data = file_item.read()
    file = {
        'file': base64.b64encode(data),
        'filename': file_item.filename,
        'link': uuid.uuid4()
    }
    file_model = _get_file_model()
    created_file = file_model.create(vals_list=[file])
    return format_link(created_file.link)


def get_file(file_link: str) -> Union[File, None]:
    """Get binary file from database."""

    file_model = _get_file_model()
    list_binary_file = file_model.search([('link', '=', file_link)])
    if not list_binary_file:
        return None
    binary_file = list_binary_file[0]
    file = File(filename=binary_file.filename,
                data=base64.decodebytes(binary_file.file))
    return file


def format_link(db_link: str) -> str:
    """Returns formatted link with host."""
    result_link = (f'{request.httprequest.host}/'
                   f'nekotopec_share/file/download/{db_link}')
    logging.info(f'FILE_LINK:\t{result_link}')
    return result_link


def _get_file_model() -> odoo.models.Model:
    """Returns model."""
    return request.env['nekotopec_share.file']
