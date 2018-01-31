from app import db
from sqlalchemy.exc import IntegrityError
from flask import Response
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(32), unique=True)

    @staticmethod
    def add_new_user(username, password):
        if username is None or password is None:
            return None # missing arguments
        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None
        res = {}
        res['user_id'] = user.id
        return res

    @staticmethod
    def login(username, password):
        if username is None or password is None:
            return None # missing arguments
        user = User.query.filter_by(username=username).first()
        if user is None:
            return None
        if user.password != password:
            return None
        res = {}
        res['user_id'] = user.id
        return res
