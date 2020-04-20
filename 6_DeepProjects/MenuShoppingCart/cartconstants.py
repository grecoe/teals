'''
    This file identifies constants should be used in your IFunction 
    instances. 
'''
import os
import json

class Categories:
    DAIRY = "dairy"
    MEAT = "meat"
    VEGETABLES = "veg"
    BREAD = "bread"
    GENERAL = "general" 

class ShoppingCart:
    LIST_PATH = "lists"

    def __init__(self, working_directory):
        self.working_directory = working_directory
        self.current_list = "UNDEFINED"
        self.shopping_cart = {}
        self.categories = [
            Categories.DAIRY,
            Categories.MEAT,
            Categories.VEGETABLES,
            Categories.BREAD,
            Categories.GENERAL
        ]

        for category in self.categories:
            self.shopping_cart[category] = []

    def get_cart(self):
        return self.shopping_cart

    def get_categories(self):
        return self.categories

    def add(self, category, items, fail_on_invalid_category = False):
        """
            Add an item or items to the shopping cart

            category = category to add to, one of the values in Categories
            items = Single item OR list of items to add
            fail_on_invalid_category:
                If True, raises an exception if the category doesn't exist, 
                otherwise add to the general category. 

            Returns : Nothing
        """
        if not category:
            category = Categories.GENERAL

        if category not in self.categories:
            if fail_on_invalid_category:
                raise Exception("Category {} not in valid category list.".format(category))
            else:
                category = Categories.GENERAL

        # Is it a list?
        item_list = []
        if isinstance(items, list):
            item_list.extend(items)
        else:
            item_list.append(items)

        # Now add them in 
        self.shopping_cart[category].extend(item_list)

    def remove(self, items):
        """
            Remove item(s) from the shopping cart

            items = Single item OR list of items to add

            Returns : Count of items removed
        """
        removed_count = 0

        items_to_remove = []
        if isinstance(items, list):
            items_to_remove.extend(items)
        else:
            items_to_remove.append(items)

        for category in self.shopping_cart.keys():
            # Go through each category
            for item in items_to_remove:
                # Go through each item to remove
                if item in self.shopping_cart[category]:
                    # If the item is present, remove all of them but
                    # get the count of items to remove. 
                    item_count = self.shopping_cart[category].count(item)
                    removed_count += item_count
                    while item_count > 0:
                        idx = self.shopping_cart[category].index(item)
                        self.shopping_cart[category].pop(idx)
                        item_count -= 1
        
        return removed_count

    def get_list_files(self):
        path = self._get_cart_path()
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    def load(self, list_name):
        path = self._get_cart_path()
        path = os.path.join(path,list_name)
        if not os.path.isfile(path):
            print("List {} does not exist".format(list_name))

        with open(path,'r') as input_file:
            lines = input_file.readlines()
            self.shopping_cart = json.loads("\n".join(lines))
        
        self.current_list = list_name
    
    def save(self, list_name):
        path = self._get_cart_path()
        path = os.path.join(path,list_name)
        with open(path,'+w') as output_file:
            output_file.write(json.dumps(self.shopping_cart, indent=4))
        self.current_list = list_name

    def _get_cart_path(self):
        path = os.path.join(self.working_directory, ShoppingCart.LIST_PATH)
        if not os.path.isdir(path):
            os.makedirs(path)
        return path

