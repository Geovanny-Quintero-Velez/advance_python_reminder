def calculate_average(numbers):
    """
    Calculate the average of a number list.

    parameters:
    numbers (list): list of int ot float

    return:
    float: average of the list's numbers
    """
    return sum(numbers) / len(numbers)

# Printing the result of the function
print(calculate_average([1,2,3,4,5]))

# Comments must not be obvious or redundant, only necessary information