from database import db
from flask_login import UserMixin #UserMixin possui varias funcionalidades pre-configuradas(is_active, is_authenticated, get_id,...), portanto o User ira herdar de UserMixin tbm

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)
  role = db.Column(db.String(80), nullable=False, default="user")