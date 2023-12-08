from os import environ

class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY')  
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')  