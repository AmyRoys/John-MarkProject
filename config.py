import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://test_user:amydb@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)