

list = [2,3,4,5,6,7,8,56,78,8]
count = 0
for i in list:
    if i % 2 == 0:
        count+=1
print("even numbers:",count)        



marks = int(input("enter the score of written test"))
lab_exam = int(input("enter the score of lab exam "))
assignment = int(input("enter the score of assignment"))

overall_grade = marks*0.7 + lab_exam*0.2 + assignment*0.1
print("Overall Grade:",overall_grade)


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



