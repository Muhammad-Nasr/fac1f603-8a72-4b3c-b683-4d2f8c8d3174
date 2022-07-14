from flask import Blueprint


error = Blueprint('errors', __name__)

from . import handlers