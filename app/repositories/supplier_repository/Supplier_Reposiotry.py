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

