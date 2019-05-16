import os
from flask import Flask
from app.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def root():
    return 'Hello World! Welcome to "/"', 200
