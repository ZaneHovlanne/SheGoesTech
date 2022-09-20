# 1c

list_numbers = []


while True:
    numbers_entered = input(
        "Please enter numbers(separated by comma) or 'q' to quit: ")
    if numbers_entered == "q":
        print("You quit")
        break

    else:
        list_numbers.append(float(numbers_entered))
        sorted_number_list = sorted(numbers_entered)
        average_calculated = sum(numbers_entered) / len(numbers_entered)
        print(
            f"Numbers you enetered are: {numbers_entered} , average is: {average_calculated}")

        print(f"Top 3 values you enetered are: {sorted_number_list[-3:]}")
        print(f"Bottom 3 values you entered are: {sorted_number_list[:3]}")


# exercise 2
start_integer = int(input("Please enter the beggining integer: "))
end_integer = int(input("Please enter the end integer: "))
numbers = list(range(start_integer, end_integer))
squares = []
for num in numbers:
    squares.append(num**2)
    print(f"{num} cubed {num**2}")
print(squares)

# task No 3
sentence_entered = input("Please enter a sentence: ")

split_sentence = sentence_entered.split()

reversed_sentence = [word[::-1] for word in split_sentence]

new_sentence = " ".join(reversed_sentence)

print(new_sentence)
