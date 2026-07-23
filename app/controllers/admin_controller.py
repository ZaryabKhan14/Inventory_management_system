class AdminContoller:

    def __init__(self,user):

        self.user = user

    def admin_dashboard(self):

        while True:

            print("\n===== ADMIN DASHBOARD =====")
            print("1. User Management")
            print("2. Category Management")
            print("3. Product Management")
            print("4. Supplier Management")
            print("5. Customer Management")
            print("6. Purchase")
            print("7. Sales")
            print("8. Reports")
            print("9. Logout")

            choice = input("Enter Choice : ")

            if choice == "1":
                print("User Module")

            elif choice == "2":
                print("Category Module")

            elif choice == "9":
                print("Logout Successfully")
                break

            else:
                print("Invalid Choice")
    