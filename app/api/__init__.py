import os
from flask import Blueprint

ABSPATH = os.path.dirname(__file__)

api = Blueprint('api', __name__, template_folder=os.path.join(ABSPATH, 'templates'))


@api.route('/')
def root():
    return 'Hello World! Welcome to "/api/"', 200
