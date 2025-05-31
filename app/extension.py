from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_jwt_extended import create_access_token , decode_token , JWTManager
db= SQLAlchemy()
csrf = CSRFProtect()
jwt = JWTManager()

