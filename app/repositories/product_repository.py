from sqlalchemy.exc import DataError
from app.models.product import Product
from app import db

class ProductRepository:
    @staticmethod
    def create(data):
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product.to_dict()
    
    @staticmethod
    def get_all_active():
        products = Product.query.filter_by(is_active=True).all()
        return [p.to_dict() for p in products]
    
    @staticmethod
    def search_by_name_or_category(query):
        products = Product.query.filter(
            (Product.name.ilike(f"%{query}%"))
            (Product.cateogry.ilike(f"%{query}%"))
        ).filter_by(is_active=True).all()
        return [p.to_dict() for p in products]