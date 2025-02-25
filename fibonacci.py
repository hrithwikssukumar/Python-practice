def fibonacci_series(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series
num_terms = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci_series(num_terms))

