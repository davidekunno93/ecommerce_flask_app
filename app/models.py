from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False, unique=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    """
    Parameters are: name, gameS, videoG, img_url, release, page_no, description, tail_id, price
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=False)
    gameSeries = db.Column(db.String, nullable=False)
    videoGame = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String)
    page_no = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    tail_id = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Numeric, nullable=False)
    added = db.relationship('User',
            secondary = 'cart',
            backref = 'added',
            lazy = 'dynamic'
            )

    def __init__(self, name, gameSeries, videoGame, img_url, release_date, page_no, description, tail_id, price):
        self.name = name
        self.gameSeries = gameSeries
        self.videoGame = videoGame
        self.img_url = img_url
        self.release_date = release_date
        self.page_no = page_no
        self.description = description
        self.tail_id = tail_id
        self.price = price

    def addProduct(self):
        db.session.add(self)
        db.session.commit()

    def add_it(self, user):
        self.added.append(user)
        db.session.commit()

    def increment(self):
        if not self.amount:
            self.amount = 1
        else:
            self.amount += 1
        db.session.commit()

    def decrement(self):
        self.amount -= 1
        db.session.commit()

    def remove_it(self, user):
        self.added.remove(user)
        db.session.commit()

    def to_dict(self):
        dic = {}
        dic["name"] = self.name 
        dic["game_series"] = self.gameSeries
        dic["video_game"] = self.videoGame
        dic["img_url"] = self.img_url
        dic["release"] = self.release_date
        dic["page"] = self.page_no
        dic["description"] = self.description
        dic["tail_id"] = self.tail_id
        dic["price"] = self.price
        return dic

cart = db.Table(
    'cart',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('product_id',db.Integer, db.ForeignKey('product.id'), nullable=False)
)