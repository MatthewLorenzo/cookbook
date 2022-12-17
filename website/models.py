from website.__init_ import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  recipes = db.relationship('Recipe')

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ingredients = db.relationship('Ingredient')

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    quantity = db.Column(db.String(10000))
    measurement = db.Column(db.String(10000))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))