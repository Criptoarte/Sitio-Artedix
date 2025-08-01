import os
from flask import Flask
from config import Config
from app_routes import bp as routes_bp
from models import db
from flask_cors import CORS
from dotenv import load_dotenv
from flask.json.provider import DefaultJSONProvider  # Solo una vez

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# CORS configuration
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Parche JSONEncoder para Flask ≥2.3
class PatchedJSONProvider(DefaultJSONProvider):
    def dumps(self, obj, **kwargs):
        return super().dumps(obj, **kwargs)

    def loads(self, s, **kwargs):
        return super().loads(s, **kwargs)

app.json = PatchedJSONProvider(app)

# MongoEngine initialization
db.init_app(app)
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    import flask
    print(f"Flask version in production: {flask.__version__}")
    app.run(debug=True, port=5000)
