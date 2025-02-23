def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage (this part would be in a separate test or use case):
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will correctly print 0

my_list_with_zero = [1, 0, 3, 0, 5]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zeros is: {average_with_zero}") #This will correctly calculate the average
