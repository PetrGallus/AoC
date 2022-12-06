#PART 1
with open("input.txt") as file:
    data = [forward for forward in file.read().split("\n")]

pohyb = 0
dive = 0
for prvek in data:
    prvek = prvek.split()
    if prvek[0] == "forward":
        pohyb += int(prvek[1])
    elif prvek[0] == "down":
        dive += int(prvek[1])
    else:
        dive -= int(prvek[1])
print("\nPART 1")
print("Hodnota forward:", pohyb)
print("Hodnota dive:", dive)
print("Vynasobeni hodnot:", pohyb*dive)

#PART 2

with open("input.txt") as file:
    data = [forward for forward in file.read().split("\n")]

pohyb = 0
dive = 0
aim = 0
for prvek in data:
    prvek = prvek.split()
    if prvek[0] == "forward":
        pohyb += int(prvek[1])
        dive += aim * int(prvek[1])
    elif prvek[0] == "down":
        aim += int(prvek[1])
    else:
        aim -= int(prvek[1])
print("\nPART 2")
print("Hodnota forward:", pohyb)
print("Hodnota dive:", dive)
print("Vynasobeni hodnot:", pohyb*dive)