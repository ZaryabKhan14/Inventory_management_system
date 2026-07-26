from app.repositories.user_reopsitory.User_Repository import UserRepository

class UserService:

    def __init__(self):

        self.user_data = UserRepository()

    def add_user_service(self,user):

        try:

            self.user_data.insert_add_user(user)
            
            print("User Saved Successfully")

        except Exception as e:

            print(f"Data Insert Failed : {e}")


    def fetch_user_data(self):

        try:

            users = self.user_data.fetch_user_data()


            print("User Fetch Successfully")

            return users


        except Exception as e:
        
            print(f"User Data Fetch Failed : {e}")

            return[]


    def fetch_user_by_id(self,user_id):

        try:

            users = self.user_data.fetch_user_by_id(user_id)

        
            print("User Fetch Successfully")

            return users

        except Exception as e:

            print(f"User Data Fetch Failed : {e}")

            return[]
