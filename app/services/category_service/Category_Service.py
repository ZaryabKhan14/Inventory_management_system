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


    @Logger.log_activity(module_name="Category")
    def show_category_by_id(self,category_id):

        try:

            category_by_id = self.repository.category_by_id(category_id)

            print("User Fetch Successfully")

            return category_by_id

        except Exception as e:

            print(f"Failed to fetch category {category_id}: {e}")

            raise e


    @Logger.log_activity(module_name="Category")
    def update_category(self,category_data,category_id):

        try:
            category_data = self.repository.update_category(category_data,category_id)

            if category_data is None:
                return None

            print(f"Category {category_id} updated successfully")


            return category_data

        except Exception as e:

            print(f"Failed to update category {category_id}: {e}")

            raise e


    @Logger.log_activity(module_name="Category")
    def delete_category(self,category_id):

        try:

            delete_category = self.repository.delete_category(category_id)

            print(f"Category {category_id} Deleted successfully")


            return delete_category

        except Exception as e:

            print(f"Failed to Deleted user {category_id}: {e}")
            raise e



    @Logger.log_activity(module_name="Category")
    def search_category(self,category_id):

        pass

        try:

            search_category_by_id = self.repository.category_by_id(category_id)

            print(f"Category {category_id} Search successfully")

            return search_category_by_id

        except Exception as e:

            print(f"Failed to Search user {category_id}: {e}")
            raise e
                