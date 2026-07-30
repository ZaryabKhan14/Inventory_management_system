from app.database.connection import DatabaseConnection
from app.models.users import Users
import logging

class UserRepository:

    # def __init__(self):
    #     # self.user = Users()
    #     pass

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

        try:

            conection = DatabaseConnection().connection()

            cursor = conection.cursor(dictionary=True)

            select_user_query = "Select u.user_id,u.user_first_name,u.user_last_name,u.user_name,u.user_email,u.user_phone_number,u.user_password,u.role_id,r.role_name,u.user_status,u.created_at,u.updated_at FROM users u INNER JOIN roles r ON u.role_id = r.role_id where u.user_id = %s;"

            cursor.execute(select_user_query,(user_id,))

            user_by_id = cursor.fetchone()

            if not user_by_id:
                print(f"User with ID {user_by_id} not found.")
                return None
            
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

        finally:
            if cursor:

                cursor.close()
            if conection:
                
                conection.close()


    def update_user(self,user_data,user_id):

        try:

            database_connection = DatabaseConnection().connection()

            cursor = database_connection.cursor()

            update_query = "UPDATE users SET user_first_name = %s ,user_last_name = %s,user_name = %s,user_email = %s,user_phone_number = %s,user_password = %s,role_id = %s,user_status = %s,updated_at = NOW() WHERE user_id = %s;"

            if cursor.rowcount == 0:
                print(f"User with ID {user_id} not found in database.")
                return False
            
            update_data = (user_data.user_first_name,
                            user_data.user_last_name,
                            user_data.user_name,
                            user_data.user_email,
                            user_data.user_phone_number,
                            user_data.user_password,
                            user_data.role,  # Selected role ID
                            user_data.user_status,
                            user_id
                            )

            cursor.execute(update_query,update_data)

            database_connection.commit()

            return True


        except Exception as e:
            if database_connection:
                database_connection.rollback()  
            raise e
        
        finally:
            if cursor:
                cursor.close()
            if database_connection:
                database_connection.close()
                

    def delete_user(self,user_id):

        try:


            database_connection = DatabaseConnection().connection()

            cursor = database_connection.cursor()

            sql_query = "DELETE FROM users WHERE user_id = %s;"

            value = (user_id,)

            cursor.execute(sql_query,value)

            database_connection.commit()

            self.logger.info(f"User {user_id} Delete successfully")
            return True


        finally:
            if cursor:
                cursor.close()

            if database_connection:
                database_connection.close()