from app.repositories.user_reopsitory.User_Repository import UserRepository
import logging
from app.utils.logger.custom_logger import Logger

class UserService:


    def __init__(self):

        self.user_repository = UserRepository()

    @Logger.log_activity(module_name="USERS")
    def add_user_service(self,user):

        try:

            result = self.user_repository.insert_add_user(user)
            
            print("User Saved Successfully")

            return result

        except Exception as e:

            print(f"Data Insert Failed : {e}")

            raise e

    @Logger.log_activity(module_name="USERS")
    def fetch_user_data(self):

        try:

            users = self.user_repository.fetch_user_data()

            print("User Fetch Successfully")

            return users


        except Exception as e:
        
            print(f"User Data Fetch Failed : {e}")

            raise e

    @Logger.log_activity(module_name="USERS")
    def fetch_user_by_id(self,user_id):

        try:

            users = self.user_repository.fetch_user_by_id(user_id)

            if users is None:

                return None


        
            print("User Fetch Successfully")

            return users

        except Exception as e:

            print(f"User Data Fetch Failed : {e}")

            raise e

    @Logger.log_activity(module_name="USERS")
    def update_user_service(self,user_data,user_id):

        try:

            update_user = self.user_repository.update_user(user_data,user_id)

            if update_user is None:
                return None

            print(f"User {user_id} updated successfully")
            return update_user

        except Exception as e:

            print(f"Failed to update user {user_id}: {e}")
            raise e


    @Logger.log_activity(module_name="USERS")
    def delete_user_service(self,user_id):


        try:

            delete_user = self.user_repository.delete_user(user_id)

            if delete_user is None:
                return None

            print(f"User {user_id} Deleted successfully")

            return delete_user

        except Exception as e:

            print(f"Failed to Deleted user {user_id}: {e}")
            raise e