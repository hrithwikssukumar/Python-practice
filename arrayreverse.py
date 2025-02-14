numbers =[12,34,54,32,76,45,86,75,36,29,42]
n=len(numbers)

for i in range(n-1):
    for j in range(n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print(f"The sorted array is :{numbers}")




