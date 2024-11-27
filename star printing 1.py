
#star printing 1-square
n = int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()  


#star printing 2-left sided triangle
n = int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


#star printing 3-reverse left sided triangle
n= int(input("enter a number"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()


#star printing 4- right sided triangle
n= int(input("enter a number"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")    
    print()


    
star printing 5- reverse right sided triangle
n= int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")    
    print()  


star printing 6-Hill pattern
n= int(input("enter a number"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()                      


star printing 7-reverse hill pattern
n= int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()            


#star printing 8-Diamond pattern
n= int(input("enter a number"))
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print() 
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()  
