
#function without argument and without return type

def add():
    a = int(input("enter two numbers"))
    b = int(input())
    sum = a + b
    print(sum)


#function with argument and without returntype

def add(a,b):

    sum = a+b
    print(sum)

x = int(input("enter two numbers"))
y = int(input())   
sum = add(x,y)




#function without argument and with returntype

def add():
    a = int(input("enter two numbers"))
    b = int(input())
    sum = a+b
    return sum


result=add()   
print(result)

   
    
#function with argument and with return type

def add(a,b):
    return a+b

x= int(input("enter two numbers"))
y = int(input())
a = add(x,y)
print(a)





    












