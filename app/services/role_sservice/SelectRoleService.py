from app.repositories.role_repository.Select_role_repository import SelectRoleRepository


class SelectRoleService:

    def __init__(self):

        self.add_user_reposiotry = SelectRoleRepository()

    def add_user(self):

        return self.add_user_reposiotry.fetch_all_roles()