from app.database.connection import DatabaseConnection
from app.models.users import Users

class AddUser:

    def __init__(self):
        # self.user = Users()
        pass

    def insert_add_user(self,user):

        try:
            connection = DatabaseConnection().connection()

            cursor = connection.cursor()

            sql_query = "INSERT INTO users (user_first_name,user_last_name,user_name,user_email,user_phone_number,user_password,role_id,user_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

            user_data = (user.user_first_name,user.user_last_name,user.user_name,user.user_email,user.user_phone_number,user.user_password,user.role,user.user_status)

            cursor.execute(sql_query,user_data)

            connection.commit()

            cursor.close()

            connection.close()

        except Exception as e:

            print(f"Data Insert Failed : {e}")

