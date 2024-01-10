# Reading the content of the uploaded file for the second part of the task.
file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    cube_games_data_part_two = file.readlines()

def calculate_minimum_set_power(subsets):
    """Calculate the power of the minimum set of cubes required for a game."""
    # Initialize minimum counts for each color
    min_red, min_green, min_blue = 0, 0, 0

    for subset in subsets:
        # Parse each subset to get the counts of each color
        counts = parse_subset(subset)
        # Update the minimum counts if necessary
        min_red = max(min_red, counts['red'])
        min_green = max(min_green, counts['green'])
        min_blue = max(min_blue, counts['blue'])

    # Calculate the power of the set
    power = min_red * min_green * min_blue
    return power

def calculate_total_power_of_minimum_sets(cube_games_data):
    """Calculate the total power of minimum sets required for all games."""
    total_power = 0
    for line in cube_games_data:
        _, subsets_str = line.strip().split(':')
        subsets = subsets_str.split(';')
        total_power += calculate_minimum_set_power(subsets)
    return total_power

# Calculating the total power of the minimum sets for all games
total_power_minimum_sets = calculate_total_power_of_minimum_sets(cube_games_data_part_two)
total_power_minimum_sets
