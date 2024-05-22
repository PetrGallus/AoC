def count_overlapping_ranges(file_content):
    count = 0

    for line in file_content:
        # Splitting the line into two ranges
        range1, range2 = line.strip().split(',')
        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))

        # Checking if the ranges overlap
        if (start1 <= end2 and end1 >= start2):
            count += 1

    return count

# Counting the number of pairs where the ranges overlap
count_overlapping_ranges(content)

