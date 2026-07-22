from app.controllers.category_controller import Category_Controller
import app.utils.helper 


controller = Category_Controller()

status = True

while status:

    print("Main Menu")

    print("1 : Add Category")

    user_choice = app.utils.helper.get_input_choice("Select Your Option : " , [1])

    match user_choice:

        case 1:
            controller.add_category()

