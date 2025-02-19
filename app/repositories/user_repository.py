from app.models.user import User
from app import db

class UserRepository:
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
        
    @staticmethod
    def create(email, password_hash):
        user = User(email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

        print("user: ", user)
        
        return user
        