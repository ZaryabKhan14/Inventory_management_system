from app.repositories.auth_repository import AuthRepository

class AuthService():

    def __init__(self):

        self.auth = AuthRepository()


    def login(self,user_name,user_password):

        return self.auth.login(user_name,user_password)