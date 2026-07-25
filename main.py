from app.controllers.category.category_controller import Category_Controller
from app.controllers.auth.auth_controller import AuthController
import app.utils.helper 


controller = Category_Controller()
auth_controller = AuthController()

status = True

while status:

    auth_controller.login()

