# Homework
from collections import Counter

string_1 = input("Please enter the string you are looking for: ")
string_2 = input("Please enter the text you are searching the string in: ")


if set(string_1) <= set(string_2):
    sorted_string_2 = sorted(string_2)
    collection = Counter(sorted_string_2)
    print(collection)

elif set(string_1) != set(string_2):
    print("Not all characters are in the second string!")
