from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.models.user import User
from app.core.security import generate_tokens, hash_password, verify_password
from app import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    if User.query.filter_by(email=email).first():
        return jsonify({ "error": "Email already exists" }), 400
    
    user = User(email=email, password_hash=hash_password(password))
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        "message": "User registered successfully"
    }), 201
    
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user.password_hash, password):
        return jsonify({ "error": "Invalid credentials" }), 401

    access_token, refresh_token = generate_tokens(user.id)
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    })