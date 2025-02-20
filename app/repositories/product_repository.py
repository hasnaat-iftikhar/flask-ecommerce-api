from app.schemas.product_schema import ProductSchema
from app.models.product import Product
from app import db

product_schema = ProductSchema()

class ProductRepository:
    @staticmethod
    def create_product(data):
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product)

    @staticmethod
    def get_all_active_products():
        products = Product.query.filter_by(is_active=True).all()
        return product_schema.dump(products, many=True)

    @staticmethod
    def update_product(id, data):
        product = Product.query.get_or_404(id)
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return product_schema.dump(product)

    @staticmethod
    def soft_delete_product(id):
        product = Product.query.get_or_404(id)
        product.is_active = False
        db.session.commit()
    
    @staticmethod
    def search_by_name_or_category(query):
        products = Product.query.filter(
            (Product.name.ilike(f"%{query}%"))
            (Product.cateogry.ilike(f"%{query}%"))
        ).filter_by(is_active=True).all()
        return [p.to_dict() for p in products]