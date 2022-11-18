from datetime import datetime
from inventorymanagement import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column("user_name", db.String(20), unique=True, nullable=False)
    email = db.Column("user_email", db.String(120), unique=True, nullable=False)
    password = db.Column("user_password", db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.user_id)