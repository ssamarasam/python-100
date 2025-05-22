# using property to replace getter and setter
# using decorator to simply the code

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         print("negative value")
    #         raise ValueError("Price cannot be zero")
    #     self.__price = value


product = Product(10)
print(product.price)
product.price = 25
print(product.price)

# if we remove the setter property, then the attribute will behave as read only
