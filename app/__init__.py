from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.core.config.Config")
    
    db.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)
    
    from app.routes.auth import auth_bp
    from app.routes.orders import orders_bp
    from app.routes.products import products_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    return app
