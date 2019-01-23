from flask import Blueprint

hello_world = Blueprint('hello_world', __name__)


@hello_world.route('/')
def index():
    return 'Hello World!', 200
