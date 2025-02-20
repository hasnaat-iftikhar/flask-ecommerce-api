from app.services.product_service import ProductService

def create_product(data):
    required_fields = ["name", "price", "stock"]
    if not all(field in data for field in required_fields):
        return ({
            "error": "Missing required fields"
        }), 400
        
    return ProductService.create(data)

def get_products():
    return ProductService.get_all()

def search_products(query):
    if not query:
        return ({
            "error": "Query parameter required"
        }), 400
    
    return ProductService.search(query)