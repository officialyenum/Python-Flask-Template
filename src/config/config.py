# config.py
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # MongoDB example
    MONGO_URI = os.getenv("MONGO_URI","mongodb://localhost:27017/mydatabase")
    # SQLAlchemy (Postgres or SQLite) example
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI","postgresql://username:password@localhost/dbname")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class ProductionConfig(Config):
    DEBUG = False
    

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}