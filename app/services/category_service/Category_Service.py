from app.repositories.category_repository.category_repository import CategoryRepository
from app.utils.logger.custom_logger import Logger

class CategoryService():

    def __init__(self):
        
        self.repository = CategoryRepository()

    
    def add_category(self,category):

        self.repository.insert_data(category)

        print("Category Saved Successfully")

    @Logger.log_activity(module_name="Category")
    def show_category(self):

        try:

            categories = self.repository.show_category()

            return categories

        except Exception as e:

            # print(f"Data Fetch Failed : {e}")

            raise 
