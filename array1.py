def find_number_in_array(array, target):

    if target in array:
        return f"{target} is present in the array."
    else:
        return f"{target} is not present in the array."


array = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search for: "))
result = find_number_in_array(array, target)
print(result)



n = int(input("Enter the size of the array: "))
numbers =[]
for i in range(n):
    num = int(input(f"Enter the {i+1}value : "))
    numbers.append(num)
target =int(input("Enter the target to find: "))
if target in numbers:
    index = numbers.index(target)
    print(f"Number found at position {index+1}")
else:
    print(f"No such numbers are present in this list")




def find_target_position(numbers, target):
    """Find the position of the target number in the list."""
    if target in numbers:
        index = numbers.index(target)  # Get first occurrence index
        return index + 1  # Convert to 1-based index
    else:
        return -1  # Return -1 if target not found

# Taking input
def main():
    n = int(input("Enter the size of the array: "))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter the {i+1} value: "))
        numbers.append(num)

    target = int(input("Enter the target to find: "))

    # Call function
    position = find_target_position(numbers, target)

    if position != -1:
        print(f"Number found at position {position}")
    else:
        print("No such number is present in this list")

# Run the program
if __name__ == "__main__":
    main()    