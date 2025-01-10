temperature = 15
if temperature > 15:
    message = 'Warm'
else:
    message = 'Cold'

print(message)

message = 'Warm' if temperature > 15 else 'Cold'
print(message)


high_income = True
salary = True
student = True

if (high_income or salary) and not student:
    print("eligible")


age = 19

if age >= 18 and age < 65:
    print("approved")

if 18 <= age <65:
    print("yes-approved")

for number in range(1, 11):
    print(number * '*', number)


print("-------")

for number in range(1, 11):
    print(number * '*', number)
    if number == 8:
        print("ended at 8")
        break

print("-------")

for number in range(1, 10, 3):
    print(number * '*')
    if number == 8:
        print("end at 8")


else:
    print("couldn't find 8")



for x in range(5):
    for y in range(3):
        # print(x, y)
        print(f"({x}, {y})")

        




print("-------")


number = 100
while number > 0:
    print(number)
    number //= 3


command = ""
while command != 'quit':
    command = input(">" )
    print(command)

print("ended")


    
