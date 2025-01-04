def reverse_integer(number):
   
    is_negative = number < 0
    number = abs(number)  

    reversed_number = int(str(number)[::-1])

    if is_negative:
        reversed_number = -reversed_number

    return reversed_number

num = int(input("Enter an integer: "))

result = reverse_integer(num)
print(f"The reversed integer is: {result}")
