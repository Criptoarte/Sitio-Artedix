from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
from config import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine(app)
