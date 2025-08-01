import os
from flask import Flask
from config import Config
from app_routes import bp as routes_bp
from models import db
from flask_cors import CORS
from dotenv import load_dotenv
from flask.json.provider import DefaultJSONProvider
import flask_mongoengine.json as mongoengine_json  # Parche interno para evitar error con app.json_encoder

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# CORS settings
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# 🩹 Parche para Flask 2.3+ JSONEncoder
class PatchedJSONProvider(DefaultJSONProvider):
    def dumps(self, obj, **kwargs):
        return super().dumps(obj, **kwargs)

    def loads(self, s, **kwargs):
        return super().loads(s, **kwargs)

app.json = PatchedJSONProvider(app)

# 🔧 Parcheo interno del método de flask-mongoengine
def safe_override_json_encoder(app):
    if hasattr(app, "json_encoder"):
        app.json_encoder = mongoengine_json._make_encoder(app.json_encoder)

mongoengine_json.override_json_encoder = safe_override_json_encoder

# Inicialización de MongoEngine
db.init_app(app)

# Rutas
app.register_blueprint(routes_bp)

# Servidor local (útil para pruebas)
if __name__ == '__main__':
    import flask
    print(f"Flask version in production: {flask.__version__}")
    app.run(debug=True, port=5000)
