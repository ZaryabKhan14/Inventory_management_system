from app.repositories.user_reopsitory.User_Repository import UserRepository
import logging

class UserService:


    def __init__(self):

        self.user_repository = UserRepository()

    def add_user_service(self,user):

        try:

            self.user_repository.insert_add_user(user)
            
            print("User Saved Successfully")

        except Exception as e:

            print(f"Data Insert Failed : {e}")


    def fetch_user_data(self):

        try:

            users = self.user_repository.fetch_user_data()

            print("User Fetch Successfully")

            return users


        except Exception as e:
        
            print(f"User Data Fetch Failed : {e}")

            return[]


    def fetch_user_by_id(self,user_id):

        try:

            users = self.user_repository.fetch_user_by_id(user_id)

        
            print("User Fetch Successfully")

            return users

        except Exception as e:

            print(f"User Data Fetch Failed : {e}")

            return[]


    def update_user_service(self,user_data,user_id):

        self.logger = logging.getLogger(__name__)


        try:

            update_user = self.user_repository.update_user(user_data,user_id)

            self.logger.info(f"User {user_id} updated successfully")
            return update_user

        except Exception as e:

            self.logger.error(f"Failed to update user {user_id}: {e}")
            return e



    def delete_user_service(self,user_id):

        self.logger = logging.getLogger(__name__)

        try:

            delete_user = self.user_repository.delete_user(user_id)

            self.logger.info(f"User {user_id} Delete successfully")

            return delete_user

        except Exception as e:

            self.logger.error(f"Failed to Delete user {user_id}: {e}")
            return e