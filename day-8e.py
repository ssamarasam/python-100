# dir() function to find the attributes and methods defind in an object

from ecommerce import arithmetic

print(dir(arithmetic))

# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'divide', 'sum']


print(arithmetic.__name__)
print(arithmetic.__file__)
print(arithmetic.__package__)
