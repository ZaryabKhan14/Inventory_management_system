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




