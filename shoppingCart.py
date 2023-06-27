import json
from pprint import pprint

class ShoppingCart():
    
    '''
    This class represents a shopping cart object. It represents a list of shopping cart items.
    When this is run it prompts the user for an input which can be one of many choices.
    It then validates with error checking that input and proceeds to the function to do that input.
    The models for this class allow you to add remove see the shopping cart and quit the program.
    I have also built-in functionality to search a mock data list for prices of given items.
    '''
    
    
    shopping_cart = {}
    
    def __init__(self):
        json_data=open('MOCK_DATA.json')
        self.data = json.load(json_data)
        json_data.close()
        self.main_menu()
    
    def main_menu(self):
        while True:
            response = input('\nWould you like to view list, add to list, remove from list, or quit? [show/add/remove/quit]: ')
            if response.lower() == 'add' or response.lower() == 'a':
                self.addItem()
            elif response.lower() == 'remove' or response.lower() == 'r':
                self.removeItem()
            elif response.lower() == 'show' or response.lower() == 's':
                self.printCart()
            elif response.lower() == 'quit' or response.lower() == 'q':
                self.printCart()
                break
            else:
                print("\nPlease enter a valid response to the questions.\n")
    
    def addItem(self):
        while True:
            item = input('\nWhat would you like to add to your shopping list?: [item] or [done] ').title()
            if item == 'Done':
                break
            while True:
                try:
                    qty = int(input('\nHow many do you need?: [qty] '))
                    break
                except:
                    print("Please enter a valid integer quantity")
                    
            price = self.search_data(item)
            self.shopping_cart[item.title()] = {'qty' : qty,
                                                'price': price}
    
    def removeItem(self):
        item = input('\nWhat would you like to remove from your shopping list?: [item] ').title()
        try:
            self.shopping_cart.pop(item)
            print(f"{item} was removed.\n")
            print(f"------------------------\n")
        except:
            print(f"{item} is not in your shopping list.\n")
            print(f"------------------------\n")
    
    def printCart(self):
        for key, value in self.shopping_cart.items():
            print(f"{key}: {value['qty']} quantity at {value['price']} per")
        print(f"------------------------\n")
    
    def search_data(self, item):
        for a in self.data:
            if item in a["product_name"]:
                return a["product_price"]
        return 'N/A'

christian_shopping_cart = ShoppingCart()