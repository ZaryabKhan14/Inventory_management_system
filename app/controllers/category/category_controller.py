from app.models.category import Category
from app.services.category_service.Category_Service import CategoryService
import app.utils.helper

class Category_Controller():

    def __init__(self):
        
        self.service = CategoryService()


    def add_category(self):

        print("Add Category")


        category_name = app.utils.helper.get_input_string("Enter Category Name")
        category_description = app.utils.helper.get_input_string("Enter Category Description")

        print("Choose Status")
        print("1 : Active")
        print("2 : InActive")

        category_status = app.utils.helper.status_input("Enter Category Status" , [1 , 2])


        category = Category(category_name=category_name,category_description=category_description,category_status=category_status)

        self.service.add_category(category)


    def view_categories(self):

        print("\n" + "=" * 50)
        print("              ALL Category")
        print("=" * 50)


        categories = self.service.show_category()

        if not categories:
            print("\nNo Category Found.")
            return


        for category in categories:

            print(f"Category ID             : {category.category_id}")
            print(f"Category Name           : {category.category_name}")
            print(f"Category Description    : {category.category_description}")
            print(f"Category Status         : {category.category_status}")
            print(f"Category Created At     : {category.created_at}")
            print(f"Category Update At      : {category.updated_at}")
            print("-" * 50)
