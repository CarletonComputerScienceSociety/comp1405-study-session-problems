"""
Problem: Given a lists of numbers, find two numbers that add up to a specific target number. If there are no pairs that add up to the target, return None.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find_two_numbers_that_sum_to_target_easy(target, numbers):
    # interare through the list of numbers
    for number_one in numbers:
        # iterate through the list of numbers again
        for number_two in numbers:
            # if the two numbers add up to the target
            if number_one + number_two == target:
                return number_one, number_two

    # if the two numbers that add up to the target are not in the list, return None
    return None

def find_two_numbers_that_sum_to_target_complex(target, numbers):
    # Instantiate a dictionary to hold the numbers and their sum
    sum_dict = {}

    # Iterate through the list of numbers and add each number to the sum dictionary
    for number in numbers:
        sum_dict[number] = number

    # Iterate through the dictionary to find the two numbers that add up to the target
    for number in numbers:
        # If the difference between the target and the current number is in the dictionary
        if target - number in sum_dict:
            # Return the tuple of the two numbers
            return (number, target - number)
        # Else if the difference between the target and the current number is not in the dictionary
        else:
            # Continue iterating through the dictionary
            continue

    # If the two numbers that add up to the target are not in the dictionary, return None
    return None


number_one, number_two = find_two_numbers_that_sum_to_target_easy(10, numbers)
print("Results: ", number_one, number_two)

none = find_two_numbers_that_sum_to_target_easy(1000, numbers)
print("Results: ", none)
