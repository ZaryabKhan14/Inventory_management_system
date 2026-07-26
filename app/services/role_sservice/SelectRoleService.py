from app.repositories.role_repository.Select_role_repository import SelectRoleRepository


class SelectRoleService:

    def __init__(self):

        self.add_user_reposiotry = SelectRoleRepository()

    def role_fetch(self):

        return self.add_user_reposiotry.fetch_all_roles()