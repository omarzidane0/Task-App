from flask import Flask , render_template , redirect , url_for , session, request , Blueprint 
from flask_sqlalchemy import SQLAlchemy
from app.routes.register.register import register_bp
from app.routes.login.login import login_bp
from app.routes.home.home import home_bp
from jinja2 import ChoiceLoader, FileSystemLoader
from app.extension import db
from flask_wtf import CSRFProtect
from flask_jwt_extended import create_access_token , decode_token , JWTManager
from app.extension import csrf
from app.extension import jwt
def createapp():

    app = Flask(__name__, template_folder="app/templates")
    app.config["SECRET_KEY"] = "testing"
    app.config['JWT_SECRET_KEY'] = 'your-secret'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    db.init_app(app)
    jwt.init_app(app)
    csrf.init_app(app)
    from flask_wtf.csrf import generate_csrf
    @app.context_processor
    def inject_csrf_token():
        return dict(csrf_token=generate_csrf())
    app.jinja_loader = ChoiceLoader([
        FileSystemLoader("app/routes/templates"),
        FileSystemLoader("routes/register/templates"),
        FileSystemLoader("routes/login/templates")
    ])
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    return app