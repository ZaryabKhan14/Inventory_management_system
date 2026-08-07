from app.database.connection import DatabaseConnection
from app.models.category import Category


class CategoryRepository():

    def insert_data(self,category):

        try:

            database_connection = DatabaseConnection().connection()

            cursor = database_connection.cursor()

            sql_query = "INSERT INTO Category (category_name,category_description,category_status) VALUES (%s, %s, %s)" 

            values = (
                category.category_name,
                category.category_description,
                category.category_status
            )
            cursor.execute(sql_query,values)

            database_connection.commit()

            cursor.close()

            database_connection.close()

        except :

            print("Data Failed to inseert in database")


    def show_category(self):

        connection = None
        cursor = None

        try:

            connection = DatabaseConnection().connection()

            cursor = connection.cursor(dictionary=True)

            fetch_query = ("SELECT c.category_id,c.category_name,c.category_description,c.category_status,c.created_at,c.updated_at FROM Category c")

            cursor.execute(fetch_query)

            category = cursor.fetchall()

            # rows = []

            # for row in  category:

            #     category_data = Category(
            #         category_id=row['category_id'],
            #         category_name=row['category_name'],
            #         category_description=row['category_description'],
            #         category_status=row['category_status'],
            #         created_at=row['created_at'],
            #         updated_at=row['updated_at'],
            #     )

            #     rows.append(category_data)

            rows = [ Category(
                    category_id=row['category_id'],
                    category_name=row['category_name'],
                    category_description=row['category_description'],
                    category_status=row['category_status'],
                    created_at=row['created_at'],
                    updated_at=row['updated_at'],
                    )
                    for row in category
                    ]

            return rows


        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def category_by_id(self,category_id):

        connection = None
        cursor = None

        try:

            connection = DatabaseConnection().connection()

            cursor = connection.cursor(dictionary=True)

            fetch_query = ("SELECT c.category_id,c.category_name,c.category_description,c.category_status,c.created_at,c.updated_at FROM Category c WHERE c.category_id = %s ")

            cursor.execute(fetch_query,(category_id,))

            category_by_id = cursor.fetchone()

            if not category_by_id:
                return[]

            rows = Category( category_id=category_by_id['category_id'],
                                    category_name=category_by_id['category_name'],
                                    category_description=category_by_id['category_description'],
                                    category_status=category_by_id['category_status'],
                                    created_at=category_by_id['created_at'],
                                    updated_at=category_by_id['updated_at'],
                                    )
            

            return rows

        finally:

            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def update_category(self,category_data,category_id):

        connection = None

        cursor = None

        try:

            connection = DatabaseConnection().connection()

            cursor = connection.cursor()

            update_query = "UPDATE Category SET category_name = %s , category_description = %s,category_status = %s WHERE category_id = %s"


            
            
            update_data = [
                category_data.category_name,
                category_data.category_description,
                category_data.category_status,
                category_id
            ] 

            cursor.execute(update_query,update_data)

            connection.commit()

            if cursor.rowcount == 0:
                print(f"User with ID {category_id} not found in database.")
                return False

            return True

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()


    def delete_category(self,category_id):

        connection = None

        cursor = None

        try:

            connection = DatabaseConnection().connection()

            cursor = connection.cursor()

            delete_query = ("Delete FROM category WHERE category_id = %s")

            value = (category_id,)

            cursor.execute(delete_query,value)

            connection.commit()

            return True

        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()



