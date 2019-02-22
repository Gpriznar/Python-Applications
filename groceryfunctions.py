from store import Store

from groceryitem import GroceryItem

list = []

def show_menu():
    print("Let's create a shopping list! ")
    print(" Press 1 to enter the name of a store: ")
    print(" Press 2 to view all stores: ")
    print(" Press 3 to add an item to a store: ")
    print(" Press Q to quit: ")

def add_store():
    store_name = input("Enter the name of a store: ")
    store = Store(store_name)
    list.append(store)

def view_store():
    for store in list:
        print(f'{list.index(store) + 1} - {store.name} - {store.items}')

def add_item():
    view_store()
    try:
        store_select = int(input(
            "Press the number corresponading to the store where you would like to add an item: "))
        item = input("What do you want to buy?: ")
    except ValueError:
            print("ERROR *** Enter a number corresponding to the store where you would like to add an item *** ERROR")
    else:
        for store in list:
            if store_select == list.index(store) + 1:
                store.items.append(GroceryItem(item))
        else:
            print("ERROR *** That store does not exist *** ERROR")
    finally:
        pass
