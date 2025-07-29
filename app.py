import os

import flask
from flask.json.provider import DefaultJSONProvider
flask.json.JSONEncoder = DefaultJSONProvider

from flask import Flask
from config import Config
from app_routes import bp as routes_bp
from models import db
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Configuración CORS global
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

db.init_app(app)

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
