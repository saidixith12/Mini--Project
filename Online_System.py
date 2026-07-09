# ---------------------------------
# Online Shopping System
# ---------------------------------

class Product:

    product_counter = 1000

    @staticmethod
    def generate_product_id():
        Product.product_counter += 1
        return Product.product_counter

    def __init__(self, name, price):
        self.product_id = Product.generate_product_id()
        self.name = name

        # Encapsulation
        self.__price = price

    def get_price(self):
        return self.__price

    def apply_discount(self, percent):
        discount = self.__price * percent / 100
        self.__price -= discount

    # Magic Method
    def __str__(self):
        return f"[{self.product_id}] {self.name} - ₹{self.__price}"


# ---------------------------------
# Electronics Product
# ---------------------------------

class Electronics(Product):

    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def __str__(self):
        parent = super().__str__()
        return f"{parent} | Warranty: {self.warranty} yrs"


# ---------------------------------
# Clothing Product
# ---------------------------------

class Clothing(Product):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        parent = super().__str__()
        return f"{parent} | Size: {self.size}"


# ---------------------------------
# Shopping System
# ---------------------------------

products = []
cart = []


def add_product():

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    p_type = input("Type (1 Electronics, 2 Clothing): ")

    if p_type == "1":
        warranty = int(input("Enter warranty years: "))
        product = Electronics(name, price, warranty)

    elif p_type == "2":
        size = input("Enter size: ")
        product = Clothing(name, price, size)

    else:
        print("Invalid type")
        return

    products.append(product)
    print("Product added!\n")


def view_products():

    if len(products) == 0:
        print("No products available")
        return

    for p in products:
        print(p)


def add_to_cart():

    pid = int(input("Enter product ID: "))

    for p in products:
        if p.product_id == pid:
            cart.append(p)
            print("Added to cart")
            return

    print("Product not found")


def view_cart():

    total = 0

    for item in cart:
        print(item)
        total += item.get_price()

    print(f"Total Bill: ₹{total}")


def menu():

    while True:

        print("\n====== Shopping Menu ======")
        print("1 Add Product")
        print("2 View Products")
        print("3 Add to Cart")
        print("4 View Cart")
        print("5 Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            add_to_cart()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            break

        else:
            print("Invalid option")


menu()