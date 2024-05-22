# Part 1: Calculating the horizontal position and depth based on the initial understanding of commands

horizontal_position = 0
depth = 0

for command in commands:
    direction, value = command.split()
    value = int(value)

    if direction == "forward":
        horizontal_position += value
    elif direction == "down":
        depth += value
    elif direction == "up":
        depth -= value

# Calculating the product of horizontal position and depth
product_initial = horizontal_position * depth



