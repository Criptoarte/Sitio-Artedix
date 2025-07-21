import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'any-secret-key')  # valor por defecto si no lo defines
    MONGO_URI = os.getenv('MONGO_URI')

    MONGODB_SETTINGS = {
        'db': 'artedix',
        'host': MONGO_URI
    }
