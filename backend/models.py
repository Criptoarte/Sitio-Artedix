from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, FloatField, IntField

db = MongoEngine()

# Modelo de usuario (opcional, para login)
class Usuario(db.Document):
    nombre = StringField(required=True)
    contrasena = StringField(required=True)

# Modelo de artista
class Artist(db.Document):
    meta = {'collection': 'artist'}
    name = StringField(required=True)
    about = StringField()
    email = StringField()
    portfolio_link = StringField()

# Modelo de Artwork
class Artwork(db.Document):
    meta = {'collection': 'artwork'}
    name = StringField(required=True)
    quantity = IntField(required=True)
    artist_id = StringField(required=True)
