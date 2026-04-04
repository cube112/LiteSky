from flask import Blueprint

bp = Blueprint('index', __name__)

from ..index import index