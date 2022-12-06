import pathlib
#PART 1
lines = pathlib.Path('input.txt').read_text().rstrip().split('\n')
print('Zadani:')
print(lines)
numbers = [int(line) for line in lines]
print('Prevod str -> int:')
print(numbers)

count = 0
for i in range(1, len(numbers)):
    if numbers[i]>numbers[i-1]:
        count += 1
print('\nVysledek prvni casti:')
print(count)

#PART 2
lines = pathlib.Path('input.txt').read_text().rstrip().split('\n')
numbers = [int(line) for line in lines]

count = 0
sum = 0
sum2 = 0
for i in range(1,len(numbers)):
    sum = numbers[i-2]+numbers[i-1]+numbers[i]
    sum2 = numbers[i-3]+numbers[i-2]+numbers[i-1]
    if sum > sum2:
        count +=1
print('\nVysledek druhe casti:')
print (count)

