# reading input data
with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

# parsing strings in our data
max = 0
count = 0
for item in data:
    if item == '':              #if there is a gap (no number in the line), dont count it
        count = 0
    else:
        num = int(item)         #making int out of given string and saves it into variable num
        count += num            #adds numbers

    if count > max:
        max = count             #if the count is greater than currently maximal count, makes it max

print("Answer to part 1:", max)