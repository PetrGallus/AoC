# The map names are parsed correctly. The KeyError might be due to the category names used in the conversion function.
# Updating the category names in the convert_through_maps function to match the parsed map names and reattempting the calculation.

def convert_through_maps(number, maps):
    """Convert a number through all the provided maps."""
    for category in ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 
                     'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 
                     'humidity-to-location map']:
        number = convert_number(number, maps[category])
    return number

# Finding the lowest location number with the updated category names
lowest_location_number = find_lowest_location(seed_numbers, maps)
lowest_location_number
