from app.repositories.user_reopsitory.Add_User_Repository import AddUser

class Adduserservice:

    def __init__(self):

        self.user_data = AddUser()

    def add_user_service(self,user):

        self.user_data.insert_add_user(user)
        
        print("User Saved Successfully")
