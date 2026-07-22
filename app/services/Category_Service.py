from app.repositories.category_repository import CategoryRepository

class CategoryService():

    def __init__(self):
        
        self.repository = CategoryRepository()

    
    def add_category(self,category):

        self.repository.insert_data(category)

        print("Category Saved Successfully")

