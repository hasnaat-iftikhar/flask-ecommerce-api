from app.repositories.user_repository import UserRepository
from app.utils.auth import hash_password, verify_password, generate_tokens

class AuthService:
    @staticmethod
    def register(email, password):
        if UserRepository.get_by_email(email):
            return { "error", "Email exists" }, 400
        
        hashed_pw = hash_password(password)
        user = UserRepository.create(email, hashed_pw)
        return { "message", "User created" }, 201
    
    @staticmethod
    def login(email, password):
        user = UserRepository.get_by_email(email)
        
        if not user or not verify_password(user.password_hash, password):
            return { "error", "Invalid credentials" }, 401
        
        return generate_tokens(user.id)