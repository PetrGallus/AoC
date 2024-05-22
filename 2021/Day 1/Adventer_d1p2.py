# Counting the number of times the sum of measurements in a three-measurement sliding window increases

window_increase_count = 0

# Iterate through the list, starting from the third element
for i in range(2, len(depths) - 1):
    # Sum of the current window
    current_sum = depths[i-1] + depths[i] + depths[i+1]
    # Sum of the previous window
    previous_sum = depths[i-2] + depths[i-1] + depths[i]

    if current_sum > previous_sum:
        window_increase_count += 1

window_increase_count


