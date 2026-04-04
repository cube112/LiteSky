from flask import Blueprint

bp = Blueprint('doc', __name__, url_prefix='/doc')

from . import doc