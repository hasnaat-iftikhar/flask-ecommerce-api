from app.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def create(data):
        return ProductRepository.create_product(data)

    @staticmethod
    def get_all():
        return ProductRepository.get_all_active_products()

    @staticmethod
    def update(id, data):
        return ProductRepository.update_product(id, data)

    @staticmethod
    def delete(id):
        ProductRepository.soft_delete_product(id)
    
    @staticmethod
    def search(query):
        return ProductRepository.search_by_name_or_category(query)