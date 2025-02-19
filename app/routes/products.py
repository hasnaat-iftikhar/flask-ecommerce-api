from flask import Blueprint, request, jsonify
from app.models.product import Product

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "price": float(p.price)
        } for p in products
    ])
