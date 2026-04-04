from flask import Blueprint

bp = Blueprint('upload', __name__, url_prefix='/upload')

from ..upload import upload
