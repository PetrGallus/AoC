# First, let's read the content of the uploaded file to understand the format of the data.
file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    content = file.readlines()


content[:10]  # Displaying first 10 lines for a brief look at the data structure.

def count_fully_contained_ranges(file_content):
    count = 0

    for line in file_content:
        # Splitting the line into two ranges
        range1, range2 = line.strip().split(',')
        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))

        # Checking if one range fully contains the other
        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            count += 1

    return count

# Counting the number of pairs where one range fully contains the other
count_fully_contained_ranges(content)
