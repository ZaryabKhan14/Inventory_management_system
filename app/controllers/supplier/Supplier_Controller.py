from app.utils.helper import get_input_string
from app.utils.helper import status_input
from app.services.Supplier_Service.Supplier_Service import SupplierService
from app.dtos.supplier_dto import CreateSupplierDTO
from pydantic import ValidationError

class SupplierController:

    def __init__(self):
        self.supplier_service = SupplierService()


    def insert_data(self):

        print("\n" + "=" * 50)
        print("              Add Supplier Details")
        print("=" * 50)

        supplier_name = get_input_string("Enter Supplier Name : ")
        supplier_contact = get_input_string("Enter Supplier Contact : ")
        supplier_email = get_input_string("Enter Supplier Email : ")
        supplier_address = get_input_string("Enter Supplier Address : ")
        supplier_description = get_input_string("Enter Supplier Description : ")
        supplier_status = status_input("Enter Supplier Status : ", [1,2])

        try:
            data = CreateSupplierDTO(
                supplier_name=supplier_name,
                supplier_contact=supplier_contact,
                supplier_email=supplier_email,
                supplier_address=supplier_address,
                supplier_description=supplier_description,
                supplier_status=supplier_status
            )

            supplier_data = data.model_dump()

            self.supplier_service.insert_supplier(supplier_data)      

            print("\n✅ Supplier added successfully!")      

        except ValidationError as e:

            print("\n❌ Invalid Input:")

            for err in e.errors():

                field = err['loc'][0]

                msg = err['msg']

                print(f" - {field}: {msg}")