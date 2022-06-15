import sys

class Restaurant:
    def __init__(self):
        self.name = 'Sharanya Groups of Restaurants Pvt Ltd.'
        self.menu = {
            'Veg': {
                'Starters': {
                    'Paneer 65': {'price': 300, 'varieties': []},
                    'French Fries': {'price': 400, 'varieties': ['Plain', 'Fried']},
                    'Baby Corn': {'price': 250, 'varieties': ['Plain', 'crispy']},
                    'Chilly Mushroom': {'price': 350, 'varieties': ['Dry', 'Wet']},
                },
                'Main Course': {
                    'Plain Rice': {'price': 149, 'varieties': []},
                    'Paneer Fried Rice': {'price': 249, 'varieties': []},
                    'Veg Biryani': {
                        'price': 300,
                        'varieties,': ['Dum', 'Handi', 'Family Pack']
                    },
                }
            },
            'Non Veg': {
                'Starters': {
                    'Apollo Fish': {'price': 300, 'varieties': []},
                    'Chicken Manchurian': {'price': 250, 'varieties': []},
                    'Hot & Crispy Chicken': {'price': 350, 'varieties': []},
                    'King Salmon Strips': {'price': 400, 'varieties': []},
                },
                'Main Course': {
                    'Chicken Biryani': {
                        'price': 300,
                        'varieties,': ['Hyd Dumnki Biryani', 'Spl Biryani', 'Family Pack']
                    },
                    'Mutton Biryani': {
                        'price': 350,
                        'varieties,': ['Hyd Dumnki Biryanu', 'Spl Biryani', 'Family Pack']
                    },
                    'Prwans Biryani': { 'price': 300, 'varieties,': []},
                    'Fish Biryani': { 'price': 400, 'varieties,': []},
                }
            }
        }
        self.item_price_map = {}
        self.total_price = 0

    def welcome_message(self):
        print('#'*80)
        print(f'             Welcome to {self.name}')
        print('#'*80)

    get_name = lambda self, name: ''.join(char.upper() for char in name if char.isalnum())

    def print_title(self, title):
        print('{0} {title}'.format(' '*10, title=title))

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
                    print(f'{item_spaces} - {item.ljust(25)}: ₹{price}')
                    self.item_price_map[self.get_name(item)] = price

        print()
        # print(self.item_price_map)

    def select_food_type(self):
        selected_food = input('Please enter the food name (Ex: Paneer 65 or paneer65): ')
        selected_food_upper = self.get_name(selected_food)
        if selected_food_upper in self.item_price_map:
            self.total_price += self.item_price_map[selected_food_upper]
            print(f'>>>>> Total price: {self.total_price}')
        else:
            print(f'>>>>> Sorry, Currently we are not serving the {selected_food}')
            sys.exit(1)

    def process(self):
        self.welcome_message()
        self.show_menu()
        self.select_food_type()


restaurant = Restaurant()
restaurant.process()
