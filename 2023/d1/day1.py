with open('input.txt') as file:
    lines = file.read().strip().split("\n")

sum = 0
def word_to_digit(word):
    dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return dict.get(word, None)

current_number = ""
for char in lines:
    if char.isalpha():
        current_number += char.lower()
    elif char.isdigit():
        current_number += char
    else:
        if current_number:
            first_digit = current_number[0] if current_number[0].isdigit() else word_to_digit(current_number[0:])
            last_digit = current_number[-1] if current_number[-1].isdigit() else word_to_digit(current_number[-1:]) 

            if (first_digit is not None) and (last_digit is not None):
                number = int(str(first_digit) + str(last_digit))
                sum += number

print ("Part 2:",sum)            
