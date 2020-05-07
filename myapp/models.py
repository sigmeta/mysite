from myapp import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.Text, nullable=False)
    password=db.Column(db.Text, nullable=False)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    created=db.Column(db.TIMESTAMP, server_default=db.text('CURRENT_TIMESTAMP'))
    title=db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author=db.relationship('User', backref="post")
