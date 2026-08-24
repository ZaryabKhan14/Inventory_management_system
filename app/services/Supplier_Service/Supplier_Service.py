from app.repositories.supplier_repository.Supplier_Reposiotry import SupplierRepository
from app.utils.logger.custom_logger import Logger

class SupplierService:

    def __init__(self):

        self.supplier_repository = SupplierRepository()

    @Logger.log_activity(module_name="Supplier_insert")
    def insert_supplier(self,supplier_data):

        try:
            self.supplier_repository.insert_supplier(supplier_data)

            print("Category Saved Successfully")

        except Exception as e:

            raise e
