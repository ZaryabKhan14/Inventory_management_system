from app.models.role import Role
class Users:


    def __init__(self,user_id,user_first_name,user_last_name,user_name,user_email,user_phone_number,user_password,role,user_status,created_at,updated_at):

        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_name = user_name
        self.user_email = user_email
        self.user_phone_number = user_phone_number
        self.user_password = user_password
        self.role = role
        self.user_status = user_status
        self.created_at = created_at
        self.updated_at = updated_at
        
        