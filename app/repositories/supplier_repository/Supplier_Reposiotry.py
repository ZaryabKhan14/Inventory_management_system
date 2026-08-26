from app.database.connection import DatabaseConnection
from app.models.supplier import Supplier

class SupplierRepository():

    def insert_supplier(self,supplier_Data):

        database = None
        cursor = None

        try:

            database = DatabaseConnection().connection()


            cursor = database.cursor()

            sql_query = "Insert INTO suppliers (supplier_name,supplier_contact,supplier_email,supplier_address,supplier_description,supplier_status) Values (%s,%s,%s,%s,%s,%s)"

            data = (supplier_Data["supplier_name"],
                supplier_Data["supplier_contact"],
                supplier_Data["supplier_email"],
                supplier_Data["supplier_address"],
                supplier_Data["supplier_description"],
                supplier_Data["supplier_status"])

            cursor.execute(sql_query,data)

            database.commit()

        finally:
            if cursor:
                cursor.close()

            if database:
                database.close() 


    def view_supplier(self):

        database_connection = None
        cursor = None

        try:

            database_connection = DatabaseConnection().connection()

            cursor = database_connection.cursor(dictionary=True)

            sql_query = "SELECT supplier_id,supplier_name,supplier_contact,supplier_email,supplier_address,supplier_description,supplier_status,created_at,updated_at FROM suppliers"

            cursor.execute(sql_query)

            fetch_sippliers = cursor.fetchall()

            rows = [
                Supplier(
                    supplier_id = row['supplier_id'],
                    supplier_name=row['supplier_name'],
                    supplier_contact=row['supplier_contact'],
                    supplier_email=row['supplier_email'],
                    supplier_address=row['supplier_address'],
                    supplier_description=row['supplier_description'],
                    supplier_status=row['supplier_status'],
                    created_at=row['created_at'],
                    updated_at=row['updated_at'],

                )
                for row in fetch_sippliers 
            ]
            return rows

        finally:
            if cursor:
                cursor.close()

            if database_connection:
                database_connection.close()
