# Let's start by reading the binary numbers from the diagnostic report

file_path = '/mnt/data/input.txt'

with open(file_path, 'r') as file:
    binary_numbers = [line.strip() for line in file]

# Display the first few binary numbers for a quick check
binary_numbers[:10]
from collections import Counter

# Initialize variables to store the gamma and epsilon rates
gamma_rate = ''
epsilon_rate = ''

# Calculate the gamma and epsilon rates
for i in range(len(binary_numbers[0])):
    bit_count = Counter([binary_number[i] for binary_number in binary_numbers])
    most_common_bit = bit_count.most_common(1)[0][0]
    least_common_bit = '1' if most_common_bit == '0' else '0'

    gamma_rate += most_common_bit
    epsilon_rate += least_common_bit

# Convert gamma and epsilon rates from binary to decimal
gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)

# Calculate the power consumption
power_consumption = gamma_rate_decimal * epsilon_rate_decimal
gamma_rate_decimal, epsilon_rate_decimal, power_consumption

def filter_numbers(numbers, criteria):
    """ Filter the numbers based on the most common or least common bit criteria. """
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            break

        bit_count = Counter([number[i] for number in numbers])
        if bit_count['0'] == bit_count['1']:
            # If 0 and 1 are equally common
            chosen_bit = '1' if criteria == 'most' else '0'
        else:
            chosen_bit = max(bit_count, key=bit_count.get) if criteria == 'most' else min(bit_count, key=bit_count.get)

        numbers = [number for number in numbers if number[i] == chosen_bit]

    return int(numbers[0], 2)

# Calculating the oxygen generator rating and CO2 scrubber rating
oxygen_generator_rating = filter_numbers(binary_numbers, 'most')
co2_scrubber_rating = filter_numbers(binary_numbers, 'least')

# Calculating the life support rating
life_support_rating = oxygen_generator_rating * co2_scrubber_rating

oxygen_generator_rating, co2_scrubber_rating, life_support_rating




