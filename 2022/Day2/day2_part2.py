with open('input.txt') as file:
    lines = file.read().strip().split("\n")

scoring = {"A": 0, "B": 1, "C": 2, "X": -1, "Y": 0, "Z": 1} #XYZ are offset

score_value = [1,2,3]

score = 0

for line in lines:
    opponent, result = [scoring[i] for i in line.split()]

    score += (result + 1) * 3
    score += score_value[(opponent + result) % 3]


print("Answer to part 2:", score)


