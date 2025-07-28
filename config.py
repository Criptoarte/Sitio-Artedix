import os

# ========== Monkey-patch JSONEncoder ==========
import flask.json
from flask.json.provider import DefaultJSONProvider

flask.json.JSONEncoder = DefaultJSONProvider
# =============================================

from flask import Flask
from flask_mongoengine import MongoEngine

class Config:
    # Ejemplo: usa tu propia URI o variables de entorno
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_URI', 'mongodb://localhost:27017/tu_db')
    }
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cambia-esto-en-produccion')

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
