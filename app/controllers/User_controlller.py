# from app.models.users import Users
# from app.services.user_service import UserServie
# from app.utils.helper import get_input_string
# from app.utils.helper import get_input_choice


# class UserController:

#     def __init__(self):

#         user_service = UserServie()


#     def add_user():

#         try:

#             user_first_name = get_input_string("Enter User Name : ")
#             user_last_name = get_input_string("Enter Last Name : ")
#             user_name = get_input_string("Enter User Name : ")
#             user_email = get_input_string("Enter User Email : ")
#             user_phone_number = get_input_string("Enter Phone Number : ")
#             user_password = get_input_string("Enter User Password : ")
#             print("1 : Admin")
#             print("2 : Manager")
#             user_role = get_input_choice("Select User Role : ",[1 , 2])

#             match user_role:

#                 case 1:
#                     return "Admin"