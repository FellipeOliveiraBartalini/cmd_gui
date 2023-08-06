import os

os.system('cls');
os.system('clear');

from classes.Menu import Menu
from classes.ComponentManager import ComponentManager

def create_component_logic():
    component_name = str(input("Enter the name of the Component: "));

    while True:
        has_css_input = input("Does the component have CSS? (y/n): ").lower()
        if has_css_input == 'y' or has_css_input == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    has_css = True if has_css_input == 'y' else False;
    print("Creating a component...")
    cm = ComponentManager();
    cm.create(component_name, has_css);

def create_context_logic():
    print('To be implemented...');
    # component_name = str(input("Enter the name of the Component: "));
    # print("Creating a component...")
    # ComponentManager.createFile(component_name);

if __name__ == "__main__":
    options = ["Create Component", "Create Context", "Exit"]
    menu = Menu(options)

    menu.display()
    choice = menu.get_choice()

    if choice == 1:
        create_component_logic()
    elif choice == 2:
        create_context_logic()
    elif choice == 3:
        print("Exiting the menu.")
