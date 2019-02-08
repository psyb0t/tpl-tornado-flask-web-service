import os
from flask import Flask
from app.api import api

ABSPATH = os.path.dirname(__file__)

app = Flask(__name__, template_folder=os.path.join(ABSPATH, 'templates'))
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def root():
    return 'Hello World! Welcome to "/"', 200
