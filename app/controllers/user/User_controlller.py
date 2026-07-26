from app.models.users import Users
from app.services.role_sservice.SelectRoleService import SelectRoleService
from app.utils.helper import get_input_string
from app.utils.helper import get_input_choice
from app.services.user_service.UserService import UserService


class UserController:

    def __init__(self):

        self.role_service = SelectRoleService()
        
        self.user_service = UserService()


    def add_user(self):

        try:

            user_first_name = get_input_string("Enter First Name : ")
            user_last_name = get_input_string("Enter Last Name : ")
            user_name = get_input_string("Enter User Name : ")
            user_email = get_input_string("Enter User Email : ")
            user_phone_number = get_input_string("Enter Phone Number : ")
            user_password = get_input_string("Enter User Password : ")

            roles = self.role_service.role_fetch()   
            print("\n--- SELECT USER ROLE ---")

            valid_role_ids = []

            for role in roles:

                print(f"{role.role_id} : {role.role_name}")
                valid_role_ids.append(role.role_id)  # e.g., [1, 2]

            
            selected_role_id = get_input_choice("Select User Role : ",valid_role_ids)

            # user_status = get_input_string("Enter User Status : ")

            print("1. Active")
            print("2. Inactive")

            status = get_input_choice("Select Status : ", [1, 2])

            user_status = "Active" if status == 1 else "Inactive"


            selected_role = next((r for r in roles if r.role_id == selected_role_id), None)

            if selected_role is None:
                print("Invalid Role Selected")
                return
        
            print(f"\nSelected Role: {selected_role.role_name} (ID: {selected_role.role_id})")


            insert_user = Users(user_first_name=user_first_name,user_last_name=user_last_name,user_name=user_name,user_email=user_email,user_phone_number=user_phone_number,user_password=user_password,role=selected_role_id,user_status=user_status)

            self.user_service.add_user_service(insert_user)


        except Exception as e:

            print(f"Error : {e}")





    def view_users(self):

        print("\n" + "=" * 50)
        print("              ALL USERS")
        print("=" * 50)

        
        users = self.user_service.fetch_user_data()

        if not users:
            print("\nNo Users Found.")
            return

        print("-" * 50)

        for row in users:

            print(f"User ID           : {row.user_id}")
            print(f"First Name        : {row.user_first_name}")
            print(f"Last Name         : {row.user_last_name}")
            print(f"Username          : {row.user_name}")
            print(f"Email             : {row.user_email}")
            print(f"Phone Number      : {row.user_phone_number}")
            print(f"Role ID           : {row.role}")
            print(f"Role Name         : {row.role_name}")
            print(f"Status            : {row.user_status}")
            print(f"Created At        : {row.created_at}")
            print(f"Updated At        : {row.updated_at}")
            print("-" * 50)



    def update_user(self):

        print("\n" + "=" * 50)
        print("              Update USERS")
        print("=" * 50)

        user_id = get_input_string("Enter User ID : ")


        user_data_by_id = self.user_service.fetch_user_by_id(user_id=user_id)

        if not user_data_by_id:
            print("\nNo Users Found.")
            return


        
        print(f"User ID           : {user_data_by_id.user_id}")
        print(f"First Name        : {user_data_by_id.user_first_name}")
        print(f"Last Name         : {user_data_by_id.user_last_name}")
        print(f"Username          : {user_data_by_id.user_name}")
        print(f"Email             : {user_data_by_id.user_email}")
        print(f"Phone Number      : {user_data_by_id.user_phone_number}")
        print(f"Role ID           : {user_data_by_id.role}")
        print(f"Role Name         : {user_data_by_id.role_name}")
        print(f"Status            : {user_data_by_id.user_status}")
        print(f"Created At        : {user_data_by_id.created_at}")
        print(f"Updated At        : {user_data_by_id.updated_at}")
        print("-" * 50)

        


          