initial_shoppinglist = ["Apples", "Bananas", "Grapes", "Grapes", "Oranges", "Watermelon", "Apples"]
print(f"The orginal list is: {initial_shoppinglist}")

shoppinglist = []

for index in initial_shoppinglist:
    if index not in shoppinglist:
        shoppinglist.append(index)

print(f"The list after removing all duplicates: {shoppinglist}")
