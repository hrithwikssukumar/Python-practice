def sum_array(array):
    if not array:
        return 0
    else:
        return array[0] + sum_array(array[1:])
    
list = [2,3]
result = sum_array(list)
print(f"The result is :{result}")






def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter the number: "))
result = factorial(n)
print(f"The factorial  is :{result} ")




