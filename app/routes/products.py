from flask import Blueprint, request
from app.controllers.product_controller import (
    create_product, get_products, search_products, update_product, delete_product
)

products_bp = Blueprint("products", __name__)

@products_bp.route("", methods=["POST"])
def create():
    return create_product(request.get_json())

@products_bp.route("", methods=["GET"])
def get_all():
    return get_products()

@products_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    return update_product(id, request.get_json())

@products_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return delete_product(id)

@products_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return search_products(query)