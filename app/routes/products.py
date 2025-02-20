from flask import Blueprint, request, jsonify
from app.controllers.product_controller import create_product, get_products, search_products

products_bp = Blueprint("products", __name__)

@products_bp.route("", methods=["POST"])
def create():
    if request.content_type != "application/json":
        return jsonify({"error": "Unsupported Media Type: Must be JSON"}), 415

    data = request.get_json()
    return create_product(data)

@products_bp.route("", methods=["GET"])
def get_all():
    return get_products()

@products_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return search_products(query)