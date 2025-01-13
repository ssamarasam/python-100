# functions
def totals(*numbers):
    total = 1
    for number in numbers:
        total *= number

    return total


# print(totals(2, 3, 4, 5, 6))


def fizzbuzz(num):
    if ((num % 3 == 0) and (num % 5 == 0)):
        print("FizzBuzz!")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num)


fizzbuzz(19)
