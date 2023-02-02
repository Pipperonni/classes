
class ShoppingCart():

    def __init__(self):
        self.products = []


    def add_product(self):
        type = input("Enter type of product: ").lower()
        brand = input("Enter brand of product: ").lower()
        quantity = input("How many would you like: ").lower()
        price = input("What is the cost of the product: ").lower()
        
        added_product = Product(type, brand, quantity, price)
        self.products.append(added_product)

    def delete_product(self):
        delete_product = input("Enter the product type would you like to decrease quantity: ").lower()

        for i in range(len(self.products)):
            if self.products[i].type == delete_product:
                change_count = input(f"How many {self.products[i].type} would you like: ").lower()
                self.products[i].quantity = change_count
                if int(self.products[i].quantity) < 1:
                    print(f"{self.products[i].type} is no longer in cart: ")
                    self.products.pop(i)
                    return

    def print_products(self):
        for info in self.products:
            print("\n")
            print(f"Type: {info.type}  Brand: {info.brand}  Quantity: {info.quantity}  Price: {info.price}")
           

    def run(self):
        while True:
            user_choice = input("What would you like to do: (add/delete/show/quit): ").lower()

            if user_choice == "add":
                self.add_product()
            elif user_choice == "delete":
                self.delete_product()
            elif user_choice == "show":
                self.print_products()
            elif user_choice == "quit":
                self.print_products()
                return
            else:
                print("Please enter a valid input.")    




class Product():

    def __init__(self, type, brand, quantity, price):
        self.type = type
        self.brand = brand
        self.quantity = quantity
        self.price = price

cart1 = ShoppingCart()
cart1.run()