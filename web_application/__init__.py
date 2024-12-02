from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
# db.Model.metadata.reflect(bind = db.engine)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
