class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " - " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")

restaurant = Restaurant("The Bistro", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Neptune's Shelf", "Seafood")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Mrs. Noodle", "Asian")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("The Grinder", "Burgers")
restaurant3.describe_restaurant()
