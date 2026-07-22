def get_input_string(message):

    while True:

        string_value = input(message.strip())
        if string_value != "":
            return string_value
        
        else:
            print("Strint cant be empty.")


def get_input_choice(message,choice):
    while True:
        value = int(input(message))

        if value in choice:
            return value
        

        else:
            print("invalid choice")


def status_input(message,choice):

     while True:

        try:
            value = int(input(message))

            if value not in choice:
                print("Invalid choice")
                continue

            if value == 1:
                return "Active"
            elif value == 2:
                return "Inactive"
        except:        

            
            print("invalid choice")

    