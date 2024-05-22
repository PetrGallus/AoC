# Let's start by reading the list of lines of vents (line segments) from the file

file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    lines_of_vents = [line.strip() for line in file]

# Converting each line of vent into a tuple of coordinates (x1, y1, x2, y2)
vent_coordinates = []
for line in lines_of_vents:
    start, end = line.split(' -> ')
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))
    vent_coordinates.append((x1, y1, x2, y2))

# Display the first few vent coordinates for a quick check
vent_coordinates[:10]
from collections import defaultdict

def mark_line_on_map(vent_map, x1, y1, x2, y2, consider_diagonals=False):
    """ Marks the line on the map. Includes diagonals if consider_diagonals is True. """
    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            vent_map[(x1, y)] += 1
    elif y1 == y2:  # Horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            vent_map[(x, y1)] += 1
    elif consider_diagonals and abs(x1 - x2) == abs(y1 - y2):  # Diagonal line at 45 degrees
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        for i in range(abs(x1 - x2) + 1):
            vent_map[(x1 + i * x_step, y1 + i * y_step)] += 1

def count_overlaps(vent_map):
    """ Counts the number of points where at least two lines overlap. """
    return sum(1 for count in vent_map.values() if count >= 2)

# Part 1: Considering only horizontal and vertical lines
vent_map_1 = defaultdict(int)
for (x1, y1, x2, y2) in vent_coordinates:
    mark_line_on_map(vent_map_1, x1, y1, x2, y2)

overlaps_part_1 = count_overlaps(vent_map_1)

# Part 2: Considering all lines (including diagonals)
vent_map_2 = defaultdict(int)
for (x1, y1, x2, y2) in vent_coordinates:
    mark_line_on_map(vent_map_2, x1, y1, x2, y2, consider_diagonals=True)

overlaps_part_2 = count_overlaps(vent_map_2)

overlaps_part_1, overlaps_part_2


