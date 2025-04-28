from flask import Flask
from config.config import config

# db = MongoEngine()
# migrate = Migrate()

class App:
    def get_app(config_mode):
        app = Flask(__name__)
        app.config.from_object(config[config_mode])
        return app