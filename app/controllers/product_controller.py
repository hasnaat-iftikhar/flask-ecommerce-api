from app.schemas.product_schema import ProductSchema
from app.services.product_service import ProductService
from marshmallow import ValidationError

product_schema = ProductSchema()

def create_product(data):
    try:
        validated_data = product_schema.load(data)
        return ProductService.create(validated_data), 201
    except ValidationError as err:
        return {"errors": err.messages}, 400

def get_products():
    products = ProductService.get_all()
    return {"data": products}, 200

def update_product(id, data):
    try:
        validated_data = product_schema.load(data, partial=True)
        return ProductService.update(id, validated_data), 200
    except ValidationError as err:
        return {"errors": err.messages}, 400

def delete_product(id):
    ProductService.delete(id)
    return {"message": "Product deleted"}, 204

def search_products(query):
    if not query:
        return ({
            "error": "Query parameter required"
        }), 400
    
    return ProductService.search(query)