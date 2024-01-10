def parse_game_data(line):
    """Parse a line of game data into a dictionary format."""
    game_id, data = line.split(': ')
    draws = data.split('; ')
    cube_counts = []
    for draw in draws:
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for color_info in draw.split(', '):
            count, color = color_info.split(' ')
            counts[color] = int(count)
        cube_counts.append(counts)
    return int(game_id.split(' ')[1]), cube_counts

def is_game_possible(game_data, max_cubes):
    """Check if a game is possible given the max number of each color of cubes."""
    for draw in game_data:
        if any(draw[color] > max_cubes[color] for color in draw):
            return False
    return True

# Reading the file
file_path = '/mnt/data/input.txt'

possible_games = []
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

with open(file_path, 'r') as file:
    for line in file:
        game_id, game_data = parse_game_data(line.strip())
        if is_game_possible(game_data, max_cubes):
            possible_games.append(game_id)

sum_of_possible_game_ids = sum(possible_games)
sum_of_possible_game_ids, possible_games
