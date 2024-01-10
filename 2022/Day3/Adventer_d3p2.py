# Re-reading the content of the uploaded file to calculate the sum of priorities for badge item types of each group.
file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    rucksack_groups = file.readlines()

def find_badge_priority(group):
    """Find the priority of the badge item type for a group of three Elves."""
    # Split the group into individual rucksacks
    rucksacks = [rucksack.strip() for rucksack in group]
    # Find the common item type in all three rucksacks
    common_items = set(rucksacks[0]).intersection(set(rucksacks[1]), set(rucksacks[2]))
    badge_item = list(common_items)[0]  # Assuming exactly one common item type
    # Calculate the priority
    return 1 + ord(badge_item) - (ord('a') if badge_item.islower() else ord('A') - 26)

# Grouping the rucksacks into sets of three
grouped_rucksacks = [rucksack_groups[i:i+3] for i in range(0, len(rucksack_groups), 3)]

# Calculating the sum of badge priorities for each group
total_badge_priority = sum(find_badge_priority(group) for group in grouped_rucksacks)
total_badge_priority

