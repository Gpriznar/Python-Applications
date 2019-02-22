import unittest

from store import Store

from groceryitem import GroceryItem

from groceryfunctions import add_store

class Test_GroceryApp(unittest.TestCase):

    def SetUp(self):
        self.groceryitem = GroceryItem()
        self.store = Store()
        print("Setup")

    def test_add_store(self):
        result = self.store.add_store("HEB")
        self.assertEqual("HEB", result)

unittest.main()
