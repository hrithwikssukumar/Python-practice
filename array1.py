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