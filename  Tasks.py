#Task 1
#Accept a char input from the user and print on the console

name = "Virat"
print(name)


#Task 2
#Accept two input from the user and print its sum

number1 = int(input("enter two numbers"))
number2 = float(input())
sum = number1 + number2

print(sum)


#Task 3
#Write a program to find the simple interest

PI = int(input("enter the value of principal amount"))
R = float(input("enter the value of interest rate"))
N = int(input("enter the no of years"))
SI = float((PI*R*N)/100)

print("simple interest is :"+str(SI))



#Task 4
#write a program to check whether a student has passed or failed on a subject after he enters therir mark is 50 out of 100

mark = float(input("enter the marks:"))
if mark > 50:
    print("Student has passed the exam") 
else:
    print("Student has failed the exam")    


#Task 5
#write a program to show the grade obatined by a student after he enters their total mark percentage

percentage = float(input("enter the percentage:"))

if percentage > 90:
    print("A")
elif percentage > 80:
    print("B")
elif percentage > 70:
    print("C")
elif percentage > 60:
    print("D")
elif percentage >50:
    print("E")
else:
    print("Student has failed")      


#Task 6
#Using the switch case write a program to accept an input number from the user and output the day as follows

number = int(input("enter a number 1-7:"))

match number:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")   
    case other:
        print("Invalid entry")

                  
                 
#Task 7
#write a program to print the multiplication table of given numbers

number = int(input("enter a number:"))

for i in range(1,11):
    print(number,"*",i,"=",number*i)


#Task 8
#write a program to find the sum of all the odd numbers for a given limit

limit = int(input("enter the limit:"))
sum = 0


for i in range(1,limit+1,2):
    sum = sum + i
print("Sum is :",sum)    



#Task 9
#write a progarm to print the pattern

n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()    


#Task 10
#write a program to interchange the values of two arrays 

list1 = [10,23,45,76,54,28]   
list2 = [23,56,76,98,45,39]
for i in range(len(list1)):
    temp = list1[i]
    list1[i] = list2[i]
    list2[i] = temp
print(list1)
print(list2) 



   



#Task 11
#write a program to find the even numbers in an list

def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = count_even_numbers(arr)
print("Number of even numbers in the array:", even_count)


#Task 12
#write a program to sort an array in descending order

def sort_descending(arr):
    return sorted(arr, reverse=True)               

arr = [5, 2, 8, 1, 9, 3, 7]
sorted_arr = sort_descending(arr)
print("Sorted array in descending order:", sorted_arr)


#Task 13
#write a program to identify the string is palindrome or not


def is_palindrome(s):
    
    s = s.lower().replace(" ", "")
    

    return s == s[::-1]


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




#Task 14
#write a program to add two dimensional arrays


def add_2d_arrays(arr1, arr2):
    
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        return None  

    result = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            result[i][j] = arr1[i][j] + arr2[i][j]

    return result


arr1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

arr2 = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]]

result = add_2d_arrays(arr1, arr2)
if result is not None:
    print("Result of adding two 2D arrays:")
    for row in result:
        print(row)
else:
    print("Arrays have different dimensions, cannot add.")




#Task 15
#write a program to accept an array and display it on the console using functions
      
def display_array(arr):
    print("Array elements:")
    for element in arr:
        print(element, end=" ")

def main():
    
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements:")
    for i in range(n):
        element = int(input())
        arr.append(element)

    display_array(arr)

if __name__ == "__main__":
    main()



#Task 16
#write a program to check whether the number is prime or not

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


#Task 17
#write a menu driven program to do the basic mathematical operations such as addition,substraction,multiplication and division
def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

num1 = int(input("enter two numbers"))
num2 = int(input())



print("Sum:",addition(num1,num2))
print("Difference:",substraction(num1,num2))
print("Product:",multiplication(num1,num2))
print("Divide:",division(num1,num2))








#Task 18
#write a program to find out the grade of a person during his academic year


marks = int(input("enter the score of written test"))
lab_exam = int(input("enter the score of lab exam "))
assignment = int(input("enter the score of assignment"))

overall_grade = marks*0.7 + lab_exam*0.2 + assignment*0.1
print("Overall Grade:",overall_grade)





#Task 19
#write a program to find out the income tax amount of a person
def calculate_income_tax(income):
    if income <= 250000:
        tax = 0
    elif 250001 <= income <= 500000:
        tax = (income - 250000) * 0.05
    elif 500001 <= income <= 1000000:
        tax = 12500 + (income - 500000) * 0.2
    else:
        tax = 112500 + (income - 1000000) * 0.3
    return tax

def main():
    try:
        income = float(input("Enter your income: "))
        if income < 0:
            print("Income cannot be negative.")
        else:
            tax = calculate_income_tax(income)
            print("Income Tax: ₹", round(tax, 2))
    except ValueError:
        print("Invalid input. Please enter a valid income.")

if __name__ == "__main__":
    main()





#Task 20
#write a program to print the following pattern using for loop
1
23
456
78910

n = 4
p = 1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()    



#Task 21
#write  a program to multiply the values of an array and store in another array

def multiply_array(arr):
    result = []
    product = 1
    for num in arr:
        product *= num
    result.append(product)
    return result

# Example usage
arr = [1, 2, 3, 45, 5]
result_array = multiply_array(arr)
print("Resulting array after multiplication:", result_array)


#Task 22
#write a program to add the values of two 2D arrays

def add_2d_arrays(arr1, arr2):
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        return None  

    result = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)
    return result


arr1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

arr2 = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]]

result_array = add_2d_arrays(arr1, arr2)
if result_array is not None:
    print("Resulting array after addition:")
    for row in result_array:
        print(row)
else:
    print("Arrays have different dimensions, cannot add.")



#Task 23
#write an object oriented program to store and display the values of a 2D array

class Array2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            print("Index out of range.")

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            print("Index out of range.")
            return None

    def display(self):
        for row in self.data:
            print(row)


# Example usage
arr = Array2D(3, 3)

# Set values
arr.set_value(0, 0, 1)
arr.set_value(0, 1, 2)
arr.set_value(0, 2, 3)
arr.set_value(1, 0, 4)
arr.set_value(1, 1, 5)
arr.set_value(1, 2, 6)
arr.set_value(2, 0, 7)
arr.set_value(2, 1, 8)
arr.set_value(2, 2, 9)

# Display array
print("Array elements:")
arr.display()





#Task 25
#write a function that returns TRUE if its parameter is divisible by 10 and FALSE otherwise

def is_divisible_by_10(number):
    return number % 10 == 0

# Example usage
num1 = 20
num2 = 21

print(is_divisible_by_10(num1))  # Output: True
print(is_divisible_by_10(num2))  # Output: False





#Task26
#write a program to copy its input to its output,replacing each string of one or more blanks by a single blank

def remove_extra_spaces(input_string):
    return ' '.join(input_string.split())

def main():
    while True:
        try:
            user_input = input("Enter a string (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                print("Program terminated.")
                break
            else:
                output_string = remove_extra_spaces(user_input)
                print("Output:", output_string)
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    main()



#Task27
#write a program to print the corresponding celsius to fahrenheit table 

dict_temp = {
    "32.0":"0.0",
    "50.0":"10.0",
    "68.0":"20.0",
    "86.0":"30.0",
    "104.0":"50.0",
    "122.0":"60.0",
    "140.0":"70.0",
    "158.0":"80.0",
    "176.0":"90.0",
    "194.0":"100.0",
    "212.0":"100.0",
    "230.0":"110.0",
    "248.0":"120.0",
    "266.0":"130.0",
    "284.0":"140.0",
    "302.0":"150.0"
    
}
print(dict_temp)

    



    







