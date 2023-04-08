with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

import math
SUM = 0
SUM2 = 0

for i in data:
    result = math.floor(int(i)/3) - 2
    SUM += result

for i in data:
    while (result2 < 3):
        result2 = math.floor(int(i)/3) - 2
        SUM2 += result2

print("Answer to part 1: ",SUM)
print("Answer to part 2: ",SUM2)