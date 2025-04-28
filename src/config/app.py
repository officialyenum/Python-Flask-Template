import importlib
import pkgutil
from flask import Flask
from flask_socketio import SocketIO
from config.config import config
import routes

class App(Flask):
    def __init__(self, config_mode):
        super().__init__(__name__)
        self.config.from_object(config[config_mode])

        # Initialize extensions
        self.mongo = None
        self.db = None
        self.socketio = SocketIO(self, cors_allowed_origins="*")

        # Register blueprints
        self.register_database()
        # Register blueprints
        self.register_blueprints()

    def register_blueprints(self):
        # pkgutil.iter_modules Loops through all .py files inside routes/ folder.
        for _, module_name, _ in pkgutil.iter_modules(routes.__path__):
            module = importlib.import_module(f'routes.{module_name}')
            # Check if the module has a blueprint
            if hasattr(module, 'bp'):
                self.register_blueprint(module.bp)
                print(f"✅ Registered blueprint: {module_name}")
            else:
                print(f"⚠️ No blueprint found in module: {module_name}")
        
    def register_database(self):
        if 'MONGO_URI' in self.config:
            from flask_pymongo import PyMongo
            self.mongo = PyMongo(self)
            print("✅ MongoDB connected via PyMongo.")
        elif 'SQLALCHEMY_DATABASE_URI' in self.config:
            from flask_sqlalchemy import SQLAlchemy
            self.db = SQLAlchemy(self)
            print("✅ SQL Database connected via SQLAlchemy.")
        else:
            print("⚠️ No database configuration found.")
            raise ValueError(f"⚠️ No database configuration found.")


    def run_app(self, host='0.0.0.0', port=5000, debug=True):
        """Run Flask app normally (without socketio)."""
        super().run(host=host, port=port, debug=debug)

    def run_with_socketio(self, host='0.0.0.0', port=5000, debug=True):
        """Run Flask app using Socket.IO server."""
        self.socketio.run(self, host=host, port=port, debug=debug)

    @classmethod
    def get_app(cls, config_mode):
        return cls(config_mode)
