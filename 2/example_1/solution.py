"""
Problem: Given a list of numbers, calculate the mean of the list.
"""

# Provided data
sum_of_numbers = 0
list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def calculate_mean():
    # Instantiate variables to hold the sum and the number of numbers in the list.
    global sum_of_numbers
    global list_of_numbers

    # Iterate through the list of numbers and add each number to the sum.
    for number in list_of_numbers:
        sum_of_numbers += number

    # Calculate the mean
    mean = sum_of_numbers / len(list_of_numbers)

    # Print the mean
    return mean


def calculate_mean_solution(list_of_numbers):
    # Instantiate variables to hold the sum and the number of numbers in the list.
    sum_of_numbers = 0

    # Iterate through the list of numbers and add each number to the sum.
    for number in list_of_numbers:
        sum_of_numbers += number

    # Calculate the mean
    mean = sum_of_numbers / len(list_of_numbers)

    # Print the mean
    return mean


# Call the mean function
mean = calculate_mean()
solution_mean = calculate_mean_solution(list_of_numbers)

# Print the mean
print(mean)
print(solution_mean)
