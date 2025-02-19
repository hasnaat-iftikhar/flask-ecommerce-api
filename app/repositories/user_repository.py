from app.models.user import User
from app import db

class UserRepository:
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
        
    @staticmethod
    def create(email, password):
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
        