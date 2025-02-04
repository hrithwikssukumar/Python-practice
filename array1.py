def find_number_in_array(array, target):
    """Check if a specific number is in the array."""
    if target in array:
        return f"{target} is present in the array."
    else:
        return f"{target} is not present in the array."


# Example usage
array = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search for: "))
result = find_number_in_array(array, target)
print(result)

