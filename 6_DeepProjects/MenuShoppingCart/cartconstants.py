'''
    This file identifies constants should be used in your IFunction 
    instances. 
'''

class Categories:
    DAIRY = "dairy"
    MEAT = "meat"
    VEGETABLES = "veg"
    BREAD = "bread"
    GENERAL = "general" 

class ShoppingCart:
    def __init__(self):
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


