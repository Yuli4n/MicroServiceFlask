import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://products_user:isis2503@10.128.0.82:5432/products_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'MySecretKey'
