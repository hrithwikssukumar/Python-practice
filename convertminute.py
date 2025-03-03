def convert_minute(number):
    hour = number // 60
    rem_minutes = number % 60
    minutes = rem_minutes/60
    time_in_hour = hour + minutes
    return f"{time_in_hour:.1f}"
    
    
n = float(input("Enter the time in minutes: "))
result = convert_minute(n)
print(f"The converted time into minutes is : {result} hours")