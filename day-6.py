sentence = "this is a common interview question"
print(sentence)
count_of_characters = {}

for char in sentence:
    if char in count_of_characters:
        count_of_characters[char] += 1
    else:
        count_of_characters[char] = 1

print(count_of_characters)
max = 0
more = ''
for key, count in count_of_characters.items():
    if count > max:
        max = count
        more = key

print(more, max)
