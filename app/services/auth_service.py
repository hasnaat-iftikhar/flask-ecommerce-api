from app.repositories.user_repository import UserRepository
from app.utils.auth import hash_password, verify_password, generate_tokens
from sqlalchemy.exc import DataError
from flask import jsonify

class AuthService:
    @staticmethod
    def register(email, password):        
        if UserRepository.get_by_email(email):
            return { "error": "Email exists" }, 400
        
        try:
            hashed_pw = hash_password(password)
            user = UserRepository.create(email, hashed_pw)
        
            return {
                "message": "User created",
                "data": {"id": user.id, "email": user.email}
            }, 201
        
        except DataError as e:
            return {
                "error": "Database error",
                "message": str(e.orig)    
            }, 400
    
    @staticmethod
    def login(email, password):
        if not email or not password:
            return { "error": "Missing email or password" }, 400
        
        user = UserRepository.get_by_email(email)
        
        if not user or not verify_password(user.password_hash, password):
            return { "error": "Invalid credentials" }, 401
        
        try:
            tokens = generate_tokens(user.id)
            
            return jsonify({
                "message": "Login request is hitted successfully",
                "tokens": tokens
            })
        
        except DataError as e:
            return {
                "error": "Database error",
                "message": str(e.orig)    
            }, 400 