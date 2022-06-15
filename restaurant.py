import sys

class Restaurant:
    def __init__(self):
        self.name = 'Sharanya Group of Restaurants Pvt Ltd.'
        self.menu = {
            'Veg': {
                'Starters': {
                    'Paneer 65': {'price': 300},
                    'French Fries': {'price': 400},
                    'Baby Corn': {'price': 250},
                    'Chilly Mushroom': {'price': 350},
                },
                'Main Course': {
                    'Plain Rice': {'price': 149},
                    'Paneer Fried Rice': {'price': 249},
                    'Veg Biryani': {'price': 300},
                }
            },
            'Non Veg': {
                'Starters': {
                    'Apollo Fish': {'price': 300},
                    'Chicken Manchurian': {'price': 250},
                    'Hot & Crispy Chicken': {'price': 350},
                    'King Salmon Strips': {'price': 400},
                },
                'Main Course': {
                    'Chicken Biryani': {'price': 300},
                    'Mutton Biryani': {'price': 350,},
                    'Prwans Biryani': {'price': 300},
                }
            }
        }
        self.item_price_map = {}
        self.total_price = 0

    get_upper_name = lambda self, name: ''.join(char.upper() for char in name if char.isalnum())

    def process(self):
        self.show_welcome_msg()
        until_user_wants_to_select_food = True
        while until_user_wants_to_select_food:
            self.show_menu()
            self.select_food_item()

    def show_welcome_msg(self):
        print('#'*80)
        print(f'             Welcome to {self.name}')
        print('#'*80)

    def show_menu(self):
        self.print_title('Menu: ')
        # food_type: Veg / Non Veg
        for food_type, main_menu in self.menu.items():
            spaces = ' '*0
            print(f'{spaces} {food_type}')

            # main_type: Startes / Main Course
            main_item_spaces = ' '*5
            for main_type, main_items in main_menu.items():
                print(f'{main_item_spaces} {main_type}')
                
                # item: Biryani etc
                for item, item_dtls in main_items.items():
                    item_spaces = ' '*10
                    price = item_dtls['price']
                    print(f'{item_spaces} - {item.ljust(25)}: ₹ {price}')
                    self.item_price_map[self.get_upper_name(item)] = price
        print()

    def select_food_item(self):
        selected_food = input('Please enter the food name (Ex: Paneer65 or Paneer 65 or paneer65): ')
        selected_food_upper = self.get_upper_name(selected_food)
        if selected_food_upper in self.item_price_map:
            self.total_price += self.item_price_map[selected_food_upper]
            self.show_bill()
        else:
            print(f'>>>>> Sorry, Currently we are not serving: {selected_food}')
        self.select_another_item()

    def select_another_item(self):
        another_item = input('Would you like to select another item? (y or n): ')
        if another_item == 'n':
            self.show_goodbye_msg()
            sys.exit(1)
    
    def show_bill(self):
        print(f'>>>>> Your Total Bill: ₹ {self.total_price}')

    def show_goodbye_msg(self):
        print()
        self.show_bill()
        print('!!! Thank you, visit again !!!')

    def print_title(self, title):
        print('{0} {title}'.format(' '*10, title=title))


restaurant = Restaurant()
restaurant.process()
