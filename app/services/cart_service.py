# cart_service.py
from app import db
from app.models import CartItem, Product
from werkzeug.exceptions import NotFound, BadRequest

class CartService:
    @staticmethod
    def get_user_cart(user_id):
        return CartItem.query.filter_by(user_id=user_id).all()

    @staticmethod
    def add_to_cart(user_id, product_id, quantity):
        product = Product.query.get(product_id)
        if not product:
            raise NotFound(f"Product with id {product_id} not found")
        
        cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)
        
        db.session.commit()
        return cart_item

    @staticmethod
    def remove_from_cart(user_id, product_id):
        cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
        if not cart_item:
            raise NotFound(f"CartItem with product id {product_id} not found")
        
        db.session.delete(cart_item)
        db.session.commit()
        return cart_item

    @staticmethod
    def update_cart_item(user_id, product_id, quantity):
        cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
        if not cart_item:
            raise NotFound(f"CartItem with product id {product_id} not found")
        
        if quantity <= 0:
            raise BadRequest("Quantity should be greater than 0")
        
        cart_item.quantity = quantity
        db.session.commit()
        return cart_item
