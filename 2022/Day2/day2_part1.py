with open('input.txt') as file:
    lines = file.read().strip().split("\n")

scoring = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}

score_value = [1,2,3]

score = 0

for line in lines:
    opponent, me = [scoring[i] for i in line.split()]

    if (me - opponent) % 3 == 1:       # if I win
        score += 6
    elif (me == opponent):
        score += 3

    score += score_value[me]


print("Answer to part 1:", score)


