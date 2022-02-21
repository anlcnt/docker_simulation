from flask import Flask
from api import api
from interface import interface

app = Flask(__name__)
app.register_blueprint(interface)
app.register_blueprint(api, url_prefix='/api')


if __name__ == 'main':
    app.run(debug=True)
