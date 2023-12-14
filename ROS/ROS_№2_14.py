# Клас "Одяг"
class Clothes: 
    # Атрибути экземпляру класу "Клієнт"
    def __init__(self, id, name, price, size): 
        self.id = id 
        self.name = name
        self.price = price
        self.size = size

# Клас "Корзина"        
class Basket: 
    # Атрибути экземпляру класу "Клієнт"
    def __init__(self):
        self.items = []

    # Метод для додавання нового предмету одягу до корзини
    def add_item(self, clothes: Clothes): 
        self.items.append(clothes)
        
    # Метод для вилучення певного предмету одягу з корзини за його ID
    def remove_item(self, id): 
        for item in self.items:
            if item.id == id:
                self.items.remove(item)
                print(f"Item '{item.name}' was removed from basket.")
                return
        print(f"Item with ID {id} was not found in the basket.")

    # Метод для отримання повного списку речей у корзині
    def all_items(self): 
        print("Basket contains:")
        for item in self.items:
            print(f"{item.id}) {item.name}")

    # Метод для отримання загальної суми цін усіх обраних товарів
    def get_total_price(self): 
         return sum(int(item.price) for item in self.items)
    
    # Методу для вилучення усіх предметів одягу з корзини 
    def clearBasket(self): 
        self.items.clear()
        print("Now your basket is empty.")

# Клас "Клієнт"
class Customer: 
    # Атрибути экземпляру класу "Клієнт"
    def __init__(self, name, basket: Basket): 
        self.name = name
        self.basket = basket

    # Метод для додавання нового предмету одягу до корзини
    def add_to_basket(self, clothes: Clothes): 
        self.basket.add_item(clothes)
        print(f"Customer {self.name} added item '{clothes.name}' to his/her basket.")

    # Метод для вилучення певного предмету одягу з корзини за його ID
    def remove_from_basket(self, clothes: Clothes):
        self.basket.remove_item(clothes.id)

    # Метод для отримання повного списку речей у корзині
    def all_clothes(self):
        self.basket.all_items()
    
    # Метод для отримання загальної суми цін усіх обраних товарів
    def checkout(self):
        total_price = self.basket.get_total_price()
        print(f"Total price of {self.name}'s clothes: {total_price}")
    
# Створення екземпляру класу "Корзина"
basket = Basket()

yourName = input('\nYour name: ') # Запит імені користувача

# Створення екземпляру класу "Клієнт"
customer = Customer(yourName, basket)

i=1 # Лічильник, за допомогою якого визначається ID речей у корзині клієнта

# Тіло програми
while True: 
    # Вивід списку опцій
    print('\nOptions:\n1 - Add clothes to basket\n2 - Remove clothes from basket\n3 - Get all clothes from the basket\n4 - Get total price\n5 - Clear the basket')
    
    choose = input('\nEnter option:') # Змінна для вибору опції, яку користувач бажає виконати
    
    # Додавання одягу до корзини при виборі "1"
    if choose == '1': 
        print(f"\nSelected option: {choose}")
        name = input('Name: ')
        
        while True: # Перевірка коректності введення значення ціни
            try:
                price = float(input('Price: '))
                if (price <= 0):
                    print("Price can't be negative or equal 0!!! Try again.")
                else:
                    break                
            except ValueError:
                print("Price must be entered as a number!!! Try again.")        
        
        size = input('Size: ')
        customer.add_to_basket(Clothes(i, name, price, size))
        i += 1
        print('')

    # Видалення певного елементу одягу з корзини при виборі "2"    
    elif choose == '2': 
        print(f"\nSelected option: {choose}")
        
        while True: # Перевірка коректності введення значення ID
            try:
                id = int(input('ID:'))
                if (price <= 0):
                    print("ID can't be negative or equal 0!!! Try again.")
                else:
                    break                
            except ValueError:
                print("ID must be entered as a number!!! Try again.")  
               
        customer.basket.remove_item(int(id))
        print('')

    # Перегляд усіх товарів у корзині користувача при виборі "3"
    elif choose == '3': 
        print(f"\nSelected option: {choose}")
        customer.all_clothes()
        print('')

    # Виведення загальної ціни всіх товарів при виборі "4"
    elif choose == '4': 
        print(f"\nSelected option: {choose}")
        customer.checkout()
        print('')

    # Видалити увесь одяг з кошику при виборі "5"
    elif choose == '5': 
        print(f"\nSelected option: {choose}")
        customer.basket.clearBasket()

    # Виведення повідомлення про некоректність введених даних, якщо корисувач вводить не число    
    else: 
        print('Please, enter numbers only!!!')