# get set methods in python

class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than zero.")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
product.price = -10
print(product.price)


# property is an object that sits in front of the attribute and allows us to get or set the value of an attribute

# 1. define a class attribute
# 2. property(fget - function to get the value of an atribyte, fset - a function to set the value of an attribute, fdel - deleting, doc)
