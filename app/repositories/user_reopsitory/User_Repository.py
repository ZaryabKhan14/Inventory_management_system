from app.database.connection import DatabaseConnection
from app.models.users import Users

class UserRepository:

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



    def fetch_user_data(self):

        database_connection = DatabaseConnection().connection()

        cursor = database_connection.cursor(dictionary=True)

        fetch_query = "SELECT u.user_id,u.user_first_name,u.user_last_name,u.user_name,u.user_email,u.user_phone_number,u.user_password,u.role_id,r.role_name,u.user_status,u.created_at,u.updated_at FROM users u INNER JOIN roles r ON u.role_id = r.role_id;"

        cursor.execute(fetch_query)
        user = cursor.fetchall()

        rows = []

        cursor.close()
        
        database_connection.close()


        for row in user:

            users_data = Users(
                user_id=row["user_id"],
                user_first_name=row["user_first_name"],
                user_last_name=row["user_last_name"],
                user_name=row["user_name"],
                user_email=row["user_email"],
                user_phone_number=row["user_phone_number"],
                user_password=row["user_password"],
                role=row["role_id"],
                role_name=row["role_name"],
                user_status=row["user_status"],
                created_at=row["created_at"],
                updated_at=row["updated_at"]
            )

            rows.append(users_data)

        return rows


    def fetch_user_by_id(self,user_id):

        conection = DatabaseConnection().connection()

        cursor = conection.cursor(dictionary=True)

        select_user_query = "Select u.user_id,u.user_first_name,u.user_last_name,u.user_name,u.user_email,u.user_phone_number,u.user_password,u.role_id,r.role_name,u.user_status,u.created_at,u.updated_at FROM users u INNER JOIN roles r ON u.role_id = r.role_id where u.user_id = %s;"


        cursor.execute(select_user_query,(user_id,))

        user_by_id = cursor.fetchone()

        cursor.close()

        conection.close()

        user_Data = Users(
                       user_id=user_by_id["user_id"],
                        user_first_name=user_by_id["user_first_name"],
                        user_last_name=user_by_id["user_last_name"],
                        user_name=user_by_id["user_name"],
                        user_email=user_by_id["user_email"],
                        user_phone_number=user_by_id["user_phone_number"],
                        user_password=user_by_id["user_password"],
                        role=user_by_id["role_id"],
                        role_name=user_by_id["role_name"],
                        user_status=user_by_id["user_status"],
                        created_at=user_by_id["created_at"],
                        updated_at=user_by_id["updated_at"]
                        )

        

        return user_Data




        




