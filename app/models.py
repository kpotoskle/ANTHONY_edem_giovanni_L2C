from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer, primary_key=True)
    nom=db.Column(db.String(50),nullable=False)
    prenom=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(150),nullable=False,unique=True)
    password=db.Column(db.String(100),nullable=False)
    def __repr__(self):
        return '<User %r>' % self.email
    

