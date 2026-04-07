from flask import Blueprint

bp = Blueprint('upload', __name__)

from . import route
