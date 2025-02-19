from flask import Blueprint, request, jsonify
from app.models.order import Order
from app import db

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
def create_order():
    data = request.get_json()
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    
    order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    
    return jsonify({"message": "Order created successfully"}), 201