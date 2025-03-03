def leap_year(year):
    base_year = 2020
    x = year - base_year
    if x % 4 ==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a  leap year")
        

n = int(input("Enter the year to check: "))
leap_year(n)