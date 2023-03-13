with open('input.txt') as file:
    lines = list(map(int,file.read().strip().split("\n")))

#part1
for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i] + lines[j] == 2020:
            print("Part 1: ",lines[i]*lines[j])

#part2
for i in range(len(lines)):
    for j in range(len(lines)):
        for k in range(len(lines)):
            if lines[i] + lines[j] + lines[k] == 2020:
                print("Part 2: ",lines[i]*lines[j]*lines[k])