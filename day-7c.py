# inheritance
# inheritence allows us to define the common behavior in one class and inherit them in other classes
# class class-name(parent-class)
# parent ot base class
# child or sub-class
# dry - dont repeat yourself


class Animal:
    def eat(self):
        print("eat")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


shark = Fish()
shark.eat()
shark.swim()

dove = Bird()
dove.eat()
dove.fly()

# every class is directly or indirectly inheited from a class named 'object'
# class Animal: ==== class Animal(object)

print('-' * 10)
print(isinstance(dove, Bird))
print(isinstance(dove, Fish))
print(isinstance(dove, Animal))
print(isinstance(dove, object))

# sub class

print(issubclass(Fish, Animal))
print(issubclass(Fish, object))
