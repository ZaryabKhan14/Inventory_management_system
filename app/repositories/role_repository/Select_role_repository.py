from app.models.users import Users
from app.models.role import Role
from app.database.connection import DatabaseConnection

class SelectRoleRepository:

    def fetch_all_roles(self):

        connection = DatabaseConnection().connection()

        cursor = connection.cursor(dictionary=True)

        select_query = "SELECT r.role_id, r.role_name, r.role_description, r.status AS role_status, r.created_at AS role_created_at, r.updated_at AS role_updated_at FROM roles r"

        cursor.execute(select_query)

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        roles = []

        for row in rows:
            
            role_object = Role(
                role_id=row["role_id"],
                role_name=row["role_name"],
                role_description=row["role_description"],
                status=row["role_status"],           # FIXED
                created_at=row["role_created_at"],   # FIXED
                updated_at=row["role_updated_at"]    # FIXED
            )            

            roles.append(role_object)

        return roles