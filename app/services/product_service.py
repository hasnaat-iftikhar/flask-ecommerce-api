from app import db
from app.models import Product
from werkzeug.exceptions import NotFound

class ProductService:
    @staticmethod
    def get_all_products(page=1, per_page=10):
        return Product.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_product(product_id):
        product = Product.query.get(product_id)
        if not product:
            raise NotFound(f"Product with id {product_id} not found")
        return product
    
    @staticmethod
    def create_product(name, description, price):
        product = Product(
            name=name,
            description=description,
            price=price
        )
        db.session.add(product)
        db.session.commit()
        return product
    
    @staticmethod
    def update_product(product_id, name=None, description=None, price=None, inventory=None):
        product = ProductService.get_product(product_id)
        
        if name:
            product.name = name
            
        if description:
            product.description = description
            
        if price is not None:
            product.price = price

        if inventory is not None:
            product.inventory = inventory
            
        db.session.commit()
        return product
    
    @staticmethod
    def delete_product(product_id):
        product = ProductService.get_product(product_id)
        db.session.delete(product)
        db.session.commit()
        return product