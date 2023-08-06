class Menu:
    def __init__(self, options):
        self.options = options

    def display(self):
        print("Menu:")
        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Select an option: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
