from app.controllers.user.User_controlller import UserController
from app.controllers.category.category_controller import Category_Controller
# from app.controllers.product.product_controller import ProductController
# from app.controllers.supplier.supplier_controller import SupplierController
# from app.controllers.customer.customer_controller import CustomerController
# from app.controllers.purchase.purchase_controller import PurchaseController
# from app.controllers.sales.sales_controller import SalesController
# from app.controllers.report.report_controller import ReportController
from app.controllers.supplier.Supplier_Controller import SupplierController


class AdminController:

    def __init__(self, user):

        self.user = user

        self.user_controller = UserController()
        self.category_controller = Category_Controller()
        # self.product_controller = ProductController()
        self.supplier_controller = SupplierController()
        # self.customer_controller = CustomerController()
        # self.purchase_controller = PurchaseController()
        # self.sales_controller = SalesController()
        # self.report_controller = ReportController()

    def admin_dashboard(self):

        while True:

            print("\n====================================")
            print("         ADMIN DASHBOARD")
            print("====================================")

            print("1. User Management")
            print("2. Category Management")
            print("3. Product Management")
            print("4. Supplier Management")
            print("5. Customer Management")
            print("6. Purchase Management")
            print("7. Sales Management")
            print("8. Reports")
            print("9. Logout")

            choice = input("\nEnter Choice : ")

            match choice:

                # ===========================
                # USER MANAGEMENT
                # ===========================
                case "1":

                    while True:

                        print("\n====================================")
                        print("        USER MANAGEMENT")
                        print("====================================")

                        print("1. Add User")
                        print("2. View Users")
                        print("3. Update User")
                        print("4. Delete User")
                        print("5. Search User")
                        print("6. Back")

                        sub_menu = input("\nEnter Choice : ")

                        match sub_menu:

                            case "1":
                                self.user_controller.add_user()

                            case "2":
                                self.user_controller.view_users()

                            case "3":
                                self.user_controller.update_user()

                            case "4":
                                self.user_controller.delete_user()

                            case "5":
                                self.user_controller.search_user()

                            case "6":
                                break

                            case _:
                                print("Invalid Choice")

                # ===========================
                # CATEGORY MANAGEMENT
                # ===========================
                case "2":

                    while True:

                        print("\n====================================")
                        print("      CATEGORY MANAGEMENT")
                        print("====================================")

                        print("1. Add Category")
                        print("2. View Categories")
                        print("3. Update Category")
                        print("4. Delete Category")
                        print("5. Search Category")
                        print("6. Back")

                        sub_menu = input("\nEnter Choice : ")

                        match sub_menu:

                            case "1":
                                self.category_controller.add_category()

                            case "2":
                                self.category_controller.view_categories()

                            case "3":
                                self.category_controller.update_category()

                            case "4":
                                self.category_controller.delete_category()

                            case "5":
                                self.category_controller.search_category()

                            case "6":
                                break

                            case _:
                                print("Invalid Choice")

                # ===========================
                # PRODUCT MANAGEMENT
                # ===========================
                case "3":
                    print("\nProduct Module Coming Soon...")

                # ===========================
                # SUPPLIER MANAGEMENT
                # ===========================
                case "4":
                    while True:

                        print("\n====================================")
                        print("      Supplier MANAGEMENT")
                        print("====================================")

                        print("1. Add Supplier")
                        print("2. View Supplier")
                        print("3. Update Supplier")
                        print("4. Delete Supplier")
                        print("5. Search Supplier")
                        print("6. Back")

                        sub_menu = input("\nEnter Choice : ")

                        match sub_menu:

                            case "1":
                                self.supplier_controller.insert_data()

                            case "2":
                                self.supplier_controller.view_suppliers()

                            # case "3":
                            #     self.category_controller.update_category()

                            # case "4":
                            #     self.category_controller.delete_category()

                            # case "5":
                            #     self.category_controller.search_category()

                            # case "6":
                            #     break

                            case _:
                                print("Invalid Choice")

                # ===========================
                # CUSTOMER MANAGEMENT
                # ===========================
                case "5":
                    print("\nCustomer Module Coming Soon...")

                # ===========================
                # PURCHASE MANAGEMENT
                # ===========================
                case "6":
                    print("\nPurchase Module Coming Soon...")

                # ===========================
                # SALES MANAGEMENT
                # ===========================
                case "7":
                    print("\nSales Module Coming Soon...")

                # ===========================
                # REPORTS
                # ===========================
                case "8":
                    print("\nReports Module Coming Soon...")

                # ===========================
                # LOGOUT
                # ===========================
                case "9":
                    print("\nLogout Successfully.")
                    break

                case _:
                    print("\nInvalid Choice.")