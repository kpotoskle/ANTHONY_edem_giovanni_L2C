from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controlers import create_app,create_database
from models import User,db

app = create_app()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)