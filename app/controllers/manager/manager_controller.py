class ManaagerController:

    def __init__(self,user):

        self.user = user

    def manager_dashboard():

        while True:

            print("\n===== MANAGER DASHBOARD =====")
            print("1. Product")
            print("2. Purchase")
            print("3. Sales")
            print("4. Logout")

            choice = input("Enter Choice : ")

            if choice == "4":
                break