# reading input data
with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

# parsing strings in our data
max = 0  
max2 = 0
max3 = 0
count = 0
for item in data:
    if item == '':              #if there is a gap (no number in the line), dont count it
        count = 0
    else:
        num = int(item)         #making int out of given string and saves it into variable num
        count += num            #adds numbers

    if count > max:             #if the count is greater than currently maximal count, makes it max
        max3 = max2
        max2 = max
        max = count            
    elif count > max2:          #second greatest var counting
        max3 = max2
        max2 = count
    elif count > max3:          #third greatest var counting
        max3 = count

print("Answer to part 1:", max)
print("Answer to part 2:", max+max2+max3)