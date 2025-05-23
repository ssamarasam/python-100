# data classes
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# p3 = Point(3, 4)
# print(p1 == p2)
# print(id(p1))
# print(id(p2))


# without defining magic mehods and when the classes doenst have any methods, we can use namedtuple module to compare items as belo

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
# Point refers to the class object
# x and y are the individual values

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p3 = Point(x=10, y=5)
print(p1 == p2)
print(p1 < p3)
print(p1.x)
# p1.x = 10 - this wont work, as we can't set attribute once we defined, or we can reintialize again like p1 = Point(x=10, y=10)
