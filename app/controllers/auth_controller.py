from app.services.auth_service import AuthService
import app.utils.helper
from app.controllers.admin_controller import AdminContoller
from app.controllers.manager_controller import ManaagerController

class AuthController():

    def __init__(self,auth_service : AuthService = None):

        self.auth_service =  AuthService()
        

    def login(self):

        try:

            user_name = app.utils.helper.get_input_string("Enter User Name : ")
            user_password = app.utils.helper.get_input_string("Enter User Password : ")

            user = self.auth_service.login(user_name=user_name,user_password=user_password)

            if user is None:
                print("Invalid Username or Password")
                return


            print(f"\nWelcome {user.user_first_name}")

            if user.role.role_name == "Admin":
                AdminContoller(user).admin_dashboard()

            elif user.role.role_name == "Manager":
                ManaagerController(user).manager_dashboard()

            else:
                print("Role Not Found")

            # return auth_login

        except Exception as e:
            print(f"Login failed: {e}")
            return None