from app.models.category import Category
from app.services.category_service.Category_Service import CategoryService
from app.utils.helper import get_input_string 
from app.utils.helper import status_input 

class Category_Controller():

    def __init__(self):
        
        self.service = CategoryService()


    def add_category(self):

        print("Add Category")


        category_name = get_input_string("Enter Category Name")
        category_description = get_input_string("Enter Category Description")

        print("Choose Status")
        print("1 : Active")
        print("2 : InActive")

        category_status = status_input("Enter Category Status" , [1 , 2])


        category = Category(category_name=category_name,category_description=category_description,category_status=category_status)

        self.service.add_category(category)


    def view_categories(self):

        print("\n" + "=" * 50)
        print("              ALL Category Details")
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


    def update_category(self):

        print("\n" + "=" * 50)
        print("              Category Details By ID")
        print("=" * 50)

        category_id = get_input_string("Enter Category ID : ")


        category_by_id = self.service.show_category_by_id(category_id=category_id)

        if not category_by_id:
            print("\nNo Category Found.")
            return


        
        print(f"Category ID             : {category_by_id.category_id}")
        print(f"Category Name           : {category_by_id.category_name}")
        print(f"Category Description    : {category_by_id.category_description}")
        print(f"Category Status         : {category_by_id.category_status}")
        print(f"Category Created At     : {category_by_id.created_at}")
        print(f"Category Update At      : {category_by_id.updated_at}")
        print("-" * 50)

        confirm = get_input_string("do you want to edit? (yes/no) : ")

        if confirm.strip().lower() in ['yes','y']:

            category_name = get_input_string("Enter Category Name : ")
            category_description = get_input_string("Enter Category Description : ")
    
            print("Choose Status")
            print("1 : Active")
            print("2 : InActive")
    
            category_status = status_input("Enter Category Status : " , [1 , 2])

            category = Category(
                category_id=category_id,
                category_name=category_name,
                category_description=category_description,
                category_status=category_status
            )

            self.service.update_category(category,category_id)
        
        
    def delete_category(self):
        

        print("\n" + "=" * 50)
        print("              Delete Category")
        print("=" * 50)

        category_id = get_input_string("Enter Category ID : ")

        confirm = get_input_string("do you want to edit? (yes/no) : ")
        
        if confirm.strip().lower() in ['yes','y']:
        

            delete_category = self.service.delete_category(category_id=category_id)

        if not delete_category:
            print("\nNo Category Found.")
            return

        return delete_category


    def search_category(self):

        print("\n" + "=" * 50)
        print("              Search Category")
        print("=" * 50)

        category_id = get_input_string("Enter Category ID : ")

        sarch_category = self.service.search_category(category_id=category_id)


        if not sarch_category:
            print("\nNo Category Found.")
            return

        print(f"Category ID             : {sarch_category.category_id}")
        print(f"Category Name           : {sarch_category.category_name}")
        print(f"Category Description    : {sarch_category.category_description}")
        print(f"Category Status         : {sarch_category.category_status}")
        print(f"Category Created At     : {sarch_category.created_at}")
        print(f"Category Update At      : {sarch_category.updated_at}")
        print("-" * 50)
        
        return sarch_category


       
            