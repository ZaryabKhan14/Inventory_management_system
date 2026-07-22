from app.models.category import Category
from app.services.Category_Service import CategoryService
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