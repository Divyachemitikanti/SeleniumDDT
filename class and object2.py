class Product:
    def __init__(self, name,price):
        self.name=name
        self.price=price

class ShoppingCart:
    def __init__(self):
        self.cart=[]

    def add_product(self,product):
        self.cart.append(product)
        print(f"Added {product.name} to the cart.")
    def remove_product(self,product_name):
        for product in self.cart:
            if product.name==product_name:
                self.cart.remove(product)
                print(f"removed {product.name} from the cart")
                return
        print(f"Product {product_name} not found in the cart")
    def calculate_total(self):
        total=sum(product.price for product in self.cart)
        print(f"Total amount:{total:.2f}")
product1=Product(name="laptop",price=999.99)
product2=Product(name="mouse",price=49.99)
product3=Product(name="keyboard",price=79.99)
cart=ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.calculate_total()
cart.remove_product("mouse")
cart.calculate_total()