
sentence = input("Enter words or phrase you want to check: ")
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1

    else:
        char_frequency[char] = 1
print(char_frequency)
