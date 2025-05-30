# numpy

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(type(array))
print(array.shape)


array = np.zeros((3, 4), dtype=int)
print(array)

array = np.ones((5, 6), dtype=int)
print(array)

array = np.full((2, 5), 7, dtype=int)
print(array)

array = np.random.random((3, 5))
print(array)

print(array[0, 1])

print(array > 0.2)

print(array[array > 0.2])

print(np.sum(array))
print(np.floor(array))
print(np.ceil(array))
print(np.round(array))

first = np.array([1, 2, 3])
second = np.array([4, 5, 6])
print(first + second)

dimensions_inch = np.array([2, 8, 9])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
