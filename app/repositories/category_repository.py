from app.database.connection import DatabaseConnection



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
