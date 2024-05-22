# Re-reading the content of the uploaded file to calculate the total Calories carried by the top three Elves.
file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    food_calories_data = file.read().split('\n\n')

# Calculating the total calories carried by each elf
calories_per_elf = [sum(map(int, elf.split())) for elf in food_calories_data if elf.strip()]

# Sorting and taking the sum of the top three
total_calories_top_three = sum(sorted(calories_per_elf, reverse=True)[:3])
total_calories_top_three

