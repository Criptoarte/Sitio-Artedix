from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, FloatField

db = MongoEngine()

# Modelo de usuario (opcional, para login)
class Usuario(db.Document):
    nombre = StringField(required=True)
    contrasena = StringField(required=True)

# Modelo de artista
class Artist(db.Document):
    meta = {'collection': 'artist'}  # Forzar el nombre exacto
    name = StringField(required=True)
    about = StringField()
    email = StringField()

# Modelo de NFT
class NFT(db.Document):
    meta = {'collection': 'nft'}  
    name = StringField(required=True)
    price = FloatField(required=True)
    category = StringField()
    file = StringField()
