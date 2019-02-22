list = []

### Classes ###

from store import Store

from groceryitem import GroceryItem

### Functions ###

from groceryfunctions import *

### Conditionals ###

user_input = ""

while user_input != "Q":
    show_menu()
    user_input = input("Enter your choice: ")

    if user_input == '1':
        add_store()
    elif user_input == '2':
        view_store()
    elif user_input == '3':
        add_item()
