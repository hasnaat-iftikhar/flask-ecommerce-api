import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    
    # initializing application with dependencies
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    logging.basicConfig(level=logging.DEBUG)
    
    # authentication
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    # products
    from app.routes.products import products_bp
    app.register_blueprint(products_bp, url_prefix="/api/product")

    return app
