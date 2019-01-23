from flask import Flask
from hello_world import hello_world

app = Flask(__name__)
app.register_blueprint(hello_world, url_prefix='/')
