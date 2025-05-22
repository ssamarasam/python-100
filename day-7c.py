# inheritance
# inheritence allows us to define the common behavior in one class and inherit them in other classes
# class class-name(parent-class)
# parent ot base class
# child or sub-class
# dry - dont repeat yourself


class Animal:
    def __init__(self):
        self.age = 1
        print("animal constructor")

    def eat(self):
        print("eat")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        print("fish constructor")
        self.weight = 10

    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


print("shark")
shark = Fish()
# shark.eat()
# shark.swim()

# since __init__ method is defined in Fish class, the base class' __init__ will be replaced
# and age attribute wont be avialbel to the fish
# user super to call any method from the parent/base class
print(shark.age)
print(shark.weight)

# print("bird")
# dove = Bird()
# dove.eat()
# dove.fly()
# print(dove.age)


# every class is directly or indirectly inheited from a class named 'object'
# class Animal: ==== class Animal(object)

# print('-' * 10)
# print(isinstance(dove, Bird))
# print(isinstance(dove, Fish))
# print(isinstance(dove, Animal))
# print(isinstance(dove, object))


# # sub class

# print(issubclass(Fish, Animal))
# print(issubclass(Fish, object))

# method overriding -  if a same function or attribute is defined in the subclass, it will replace the function or attribute from the base class
# to use the attributes from the base class , use super method to call any method from the base class

# multi-level inheritence is bad as it increases complexity

# muliple inheritence
# class parent-class-1:
# class parent-class-2:

# class child(patent-1, parent-2)
# here child looks for the attributes or methods as per the order mentioned in the inheritance
# so, if the same method is defined in both the parent classes, child class will inheirt from parent-class-1 or whatever the parenet class mentioned first in the order

# multiple inherice can be used well when parenet classes contain unique methods to each other
