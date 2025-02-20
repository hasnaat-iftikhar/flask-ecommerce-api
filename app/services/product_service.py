from app.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def create(data):
        return ProductRepository.create(data)
    
    @staticmethod
    def get_all():
        return ProductRepository.get_all_active()
    
    @staticmethod
    def search(query):
        return ProductRepository.search_by_name_or_category(query)