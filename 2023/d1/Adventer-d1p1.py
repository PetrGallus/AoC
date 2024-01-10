# Let's read the new input data from the provided file to understand its format and content.
with open(file_path, 'r') as file:
    calibration_data = file.readlines()

# Function to extract and sum calibration values from each line
def sum_calibration_values(data):
    total_sum = 0
    for line in data:
        digits = [char for char in line if char.isdigit()]
        if digits:
            # Combine the first and last digit to form a two-digit number
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value
    return total_sum

# Calculating the sum of calibration values
sum_of_calibration_values = sum_calibration_values(calibration_data)
sum_of_calibration_values
