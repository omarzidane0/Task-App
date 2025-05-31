from flask import Flask , render_template , redirect , url_for , session, request , Blueprint
from flask_sqlalchemy import SQLAlchemy
from app import createapp
from app.extension import db
if __name__ == "__main__":
    app = createapp()
    with app.app_context():
        db.create_all()
    app.run(debug=True)