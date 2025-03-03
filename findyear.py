n = int(input("Enter the number of days: "))
year = n // 365
remaining_days = n % 365
months = remaining_days // 30
days = remaining_days % 30
print(f"The {n} days are equals to {year} years ,{months} months and {days} days")





def find_year(number):
    year = number // 365
    rem_days = number % 365
    months = rem_days // 30
    days = rem_days % 30
    
    print(f"The {n} days equals to {year} years {months} months and {days } days ")
    
n = int(input("Enter the number of days: "))
find_year(n)
