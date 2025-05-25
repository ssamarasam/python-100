import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices("abcdefgh", k=4))
print("".join(random.choices("abcdefgh", k=4)))
print("".join(random.choices(string.ascii_letters + string.digits, k=5)))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
