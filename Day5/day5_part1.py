N = 9                                           # 9 stacks of boxes
drawing_lines = 8
with open("input.txt") as file:
    parts = file.read()[:-1].split("\n\n")
    drawing = parts[0].split("\n")              #drawing = each line of cargo scheme (drawing[0] = BLS, drawing [1] = QJCWF etc....)
    #print(drawing)
    stacks = [[] for _ in range(N)]

    for i in range(drawing_lines):
        line = drawing[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks[s].append(crates[s])

stacks = [stack[::-1] for stack in stacks]      #reverse all stacks to be able to switch crate to TOP of another stack....
#print(stacks)

for line in parts[1].split("\n"):
    tokens = line.split(" ")
    n, source, destination = map(int, [tokens[1], tokens[3], tokens[5]])        #for example on first "move 8 from 7 to 1" - n=8, source=7, destination=1
    source -= 1
    destination -= 1

    for _ in range(n):
        pop = stacks[source].pop()
        stacks[destination].append(pop)


topcrates = [stack[-1] for stack in stacks]
print("Answer to part 1:", "".join(topcrates))