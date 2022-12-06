with open("input.txt") as file:
    data = file.read().strip()
    
i = 0
while True:
    marker = data[i:(i+4)]
    if len(set(list(marker))) == 4:
        print("Answer to part 1:", i+4)
        break
    i += 1
    
j = 0
while True:
    marker = data[j:(j+14)]
    if len(set(list(marker))) == 14:
        print("Answer to part 2:", j+14)
        break
    j += 1