number = int(input("Enter the number"))
is_prime = True
for i in range(2,int(number**0.5)+1):
    if number%i ==0:
        is_prime = False
        break
if is_prime:
    print("number is prime")
else:
    print("number is not prime")





def prime(number):
    if number < 2:
        return f"Enter a number greter than 2:"
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return f"The {number} is not prime"
    return f"The {number} is prime"    
    
n = int(input("Enter a number: "))
result = prime(n)
print(result)    