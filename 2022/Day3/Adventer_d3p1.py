# Reading the content of the uploaded file to find the sum of priorities of the common items in rucksacks.
file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    rucksack_contents = file.readlines()

def find_common_item_priority(rucksack):
    """Find the priority of the common item type in a rucksack."""
    half = len(rucksack) // 2
    first_compartment = set(rucksack[:half])
    second_compartment = set(rucksack[half:])
    common_items = first_compartment.intersection(second_compartment)
    return sum(1 + ord(item) - (ord('a') if item.islower() else ord('A') - 26) for item in common_items)

# Calculating the sum of priorities of common items in each rucksack
total_priority = sum(find_common_item_priority(rucksack.strip()) for rucksack in rucksack_contents)
total_priority

