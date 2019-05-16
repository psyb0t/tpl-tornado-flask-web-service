import os
from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/')
def root():
    return 'Hello World! Welcome to "/api/"', 200
