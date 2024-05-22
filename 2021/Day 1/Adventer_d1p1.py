# Let's start by reading the file content to analyze the depth measurements
file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    depths = [int(line.strip()) for line in file]

depths[:10]  # Display the first 10 measurements for a quick check
# Counting the number of times a depth measurement increases from the previous measurement

increase_count = 0

# Iterate through the list, starting from the second element
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        increase_count += 1

increase_count


