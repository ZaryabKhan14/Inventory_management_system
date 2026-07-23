from app.models.role import Role
from app.models.users import Users
from app.database.connection import DatabaseConnection


class AuthRepository:

    def login(self,user_name,user_password):

        database_connection = DatabaseConnection().connection()

        cursor = database_connection.cursor(dictionary=True)

        sql_query = """SELECT
                    u.user_id,
                    u.user_first_name,
                    u.user_last_name,
                    u.user_name,
                    u.user_email,
                    u.user_phone_number,
                    u.user_password,
                    u.user_status,
                    u.created_at,
                    u.updated_at,

                    r.role_id,
                    r.role_name,
                    r.role_description,
                    r.status AS role_status,
                    r.created_at AS role_created_at,
                    r.updated_at AS role_updated_at
                FROM users u
                INNER JOIN roles r
                    ON u.role_id = r.role_id
                WHERE u.user_name = %s
                AND u.user_password = %s
        """


        cursor.execute(sql_query, (user_name, user_password))

        print("Username:", user_name)
        print("Password:", user_password)

        row = cursor.fetchone()

        cursor.close()

        database_connection.close()

        if row is None:

            return None

        role = Role(

        row["role_id"],

        row["role_name"],

        row["role_description"],

        row["role_status"],

        row["role_created_at"],

        row["role_updated_at"]

    )

        user = Users(

            row["user_id"],

            row["user_first_name"],

            row["user_last_name"],

            row["user_name"],

            row["user_email"],

            row["user_phone_number"],

            row["user_password"],

            role,

            row["user_status"],

            row["created_at"],

            row["updated_at"]

        )


        return user