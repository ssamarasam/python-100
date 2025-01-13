# data structures
# lists []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
zeroes = [0] * 10

print(letters)
print(zeroes)
print(len(zeroes))

number = list(range(1, 21))
print(number)
print(zeroes + letters)
print(list("hello world"))
print(number[::2])
print(number[::-1])

numbers_list = [1, 2, 43, 5, 6, 7, 87, 84, 3, 2, 5, 6,  5, 6, 7, 19]
first, *others, last = numbers_list
print(first)
print(last)
print(others)


# enumurate will return a tuple

for letter in letters:
    print(letter)


print('------------')

for letter in enumerate(letters):
    print(letter)


print('------------')
for index, letter in enumerate(letters):
    print(index)

print('------------')

# add
letters.append("abcd")
print(letters)
print()

letters.insert(0, 'one')
print(letters)
print()

# remove
letters.pop()
print(letters)
letters.pop(2)
print(letters)

print()

letters.remove('c')

print(letters)
print()

del letters[2:4]
print(letters)

# letters.clear()
print(letters)
print()

# find
print(letters)
print(letters.index('a'))

if 'e' in letters:
    print(letters.index('e'))
else:
    print(f"letter 'e' is not present.")

print()

print(letters.count("z"))
print('------------------------------')

# sort
counts = [13, 51, 8, 3, 1, 87, 27, 21, 17]

counts.sort()
print(counts)

counts.sort(reverse=True)
print(counts)
print()
# above sort foucntion will modify the list

# sorted() will  return a new list without modifying the original list
counts_two = [13, 51, 8, 3, 1, 87, 27, 21, 17]
new_counts = sorted(counts_two, reverse=True)
print(counts_two)
print(new_counts)
print()
print('********************')


# sort using key
items = [
    ('product1', 100),
    ('product2', 20),
    ('product3', 31)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
print(' ')


# lambda function
# (key=lambda parameters:expression)
print('lambda-------------------')
products = [
    ('product1', 100),
    ('product2', 201),
    ('product3', 31)
]

products.sort(key=lambda item: item[1])
print(products)
