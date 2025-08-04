import os

# Monkey-patch JSONEncoder 
import flask.json
from flask.json.provider import DefaultJSONProvider

flask.json.JSONEncoder = DefaultJSONProvider

from flask import Flask
from flask_mongoengine import MongoEngine

class Config:
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_URI', 'mongodb+srv://cripto:1@cluster0.kgtnxvp.mongodb.net/artedix?retryWrites=true&w=majority')
    }
    SECRET_KEY = os.environ.get('SECRET_KEY', 'any-secret-key')

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Rutas de ejemplo
    @app.route('/')
    def hello():
        return '¡Hola, mundo!'

    return app
