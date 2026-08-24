from app.repositories.auth_repository.auth_repository import AuthRepository
from app.utils.logger.custom_logger import Logger

class AuthService():

    def __init__(self):

        self.auth = AuthRepository()

    @Logger.log_activity(module_name="Login")
    def login(self,user_name,user_password):

        return self.auth.login(user_name,user_password)