from app.models.users import Users
from app.services.role_sservice.SelectRoleService import SelectRoleService
from app.models.users import Users
from app.utils.helper import get_input_string
from app.utils.helper import get_input_choice
from app.services.user_service.AddUserService import Adduserservice


class UserController:

    def __init__(self):

        self.user_service = SelectRoleService()
        
        self.insert_user_data = Adduserservice()


    def add_user(self):

        # try:

            user_first_name = get_input_string("Enter First Name : ")
            user_last_name = get_input_string("Enter Last Name : ")
            user_name = get_input_string("Enter User Name : ")
            user_email = get_input_string("Enter User Email : ")
            user_phone_number = get_input_string("Enter Phone Number : ")
            user_password = get_input_string("Enter User Password : ")

            roles = self.user_service.add_user()   
            print("\n--- SELECT USER ROLE ---")

            valid_role_ids = []

            for role in roles:

                print(f"{role.role_id} : {role.role_name}")
                valid_role_ids.append(role.role_id)  # e.g., [1, 2]

            
            selected_role_id = get_input_choice("Select User Role : ",valid_role_ids)

            user_status = get_input_string("Enter User Status : ")


            selected_role = next((r for r in roles if r.role_id == selected_role_id), None)
        
            print(f"\nSelected Role: {selected_role.role_name} (ID: {selected_role.role_id})")


            insert_user = Users(user_first_name=user_first_name,user_last_name=user_last_name,user_name=user_name,user_email=user_email,user_phone_number=user_phone_number,user_password=user_password,role=selected_role_id,user_status=user_status)

            self.insert_user_data.add_user_service(insert_user)
            
         

          