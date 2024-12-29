
# Task 1

n=int(input("enter a number"))
fact=1

for i in range(1,n+1):
    fact=fact*i 

print(fact) 


# Task 2

n=int(input("enter a number"))
print(f"multiplication table for {n} :")
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


# Task 3

n = int(input("Enter a number: "))
if n < 2:  
    print(f"{n} is not a prime number.")
else:
    flag = 0
    for i in range(2, int(n**0.5) + 1):
  
        if n % i == 0: 
            flag = 1
            break
    if flag == 0:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

# Task 4

num_terms = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(num_terms):  # Repeat for the number of terms
    print(a, end=" ")       # Print the current term
    a, b = b, a + b   
    
    
    
    
# Task 5
for i in range(7):
    for j in range(6):
        if(i==0 or i==2 or i==4 or i==6 or j==0 ):
            print("* ",end="")
        else:
            print(" " ,end="")
    print()           # Update values: next term = sum of previous two



