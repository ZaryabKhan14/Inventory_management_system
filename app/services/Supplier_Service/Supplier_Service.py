from app.repositories.supplier_repository.Supplier_Reposiotry import SupplierRepository
from app.utils.logger.custom_logger import Logger

class SupplierService:

    def __init__(self):

        self.supplier_repository = SupplierRepository()

    @Logger.log_activity(module_name="Supplier_insert")
    def insert_supplier(self,supplier_data):

        try:
            self.supplier_repository.insert_supplier(supplier_data)

            print("Supplier Data Insert Successfully")

        except Exception as e:

            raise e

    @Logger.log_activity(module_name="Fetch_Suppliers")
    def fetch_suppliers_data(self):

        try:

            suppliers_data_fetch = self.supplier_repository.view_supplier()

            return suppliers_data_fetch

        except Exception as e:
            raise e