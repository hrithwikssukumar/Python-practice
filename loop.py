
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



