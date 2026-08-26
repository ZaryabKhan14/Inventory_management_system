from app.utils.helper import get_input_string
from app.utils.helper import status_input
from app.services.Supplier_Service.Supplier_Service import SupplierService
from app.dtos.supplier_dto import CreateSupplierDTO
from pydantic import ValidationError
from rich.table import Table
from rich.console import Console


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


    def view_suppliers(self):

        # print("\n" + "=" * 50)
        # print("              View Supplier Details")
        # print("=" * 50)


        suppliers_data = self.supplier_service.fetch_suppliers_data()

        console = Console()


        if not suppliers_data:
            console.print("[yellow]No suppliers found.[/yellow]")
            return

        # for suppliers in suppliers_data:

        #     print(f"Supplier ID                 : {suppliers.supplier_id}")
        #     print(f"Supplier Name               : {suppliers.supplier_name}")
        #     print(f"Supplier Contact            : {suppliers.supplier_contact}")
        #     print(f"Supplier Email              : {suppliers.supplier_email}")
        #     print(f"Supplier Address            : {suppliers.supplier_address}")
        #     print(f"Supplier Description        : {suppliers.supplier_description}")
        #     print(f"Supplier Status             : {suppliers.supplier_status}")
        #     print(f"Supplier Created At         : {suppliers.created_at}")
        #     print(f"Supplier Updated At         : {suppliers.updated_at}")
        #     print("-" * 50)
        table = Table(
        title="Supplier Details",
        show_header=True,
        header_style="bold cyan"
    )

        table.add_column("ID", justify="center")
        table.add_column("Name")
        table.add_column("Contact")
        table.add_column("Email")
        table.add_column("Address")
        table.add_column("Status")
        table.add_column("Created At")
        table.add_column("Updated At")

        for supplier in suppliers_data:

            table.add_row(
                str(supplier.supplier_id),
                supplier.supplier_name,
                supplier.supplier_contact,
                supplier.supplier_email,
                supplier.supplier_address,
                str(supplier.supplier_status),
                str(supplier.created_at),
                str(supplier.updated_at)
            )

        console.print(table)


