def count_up_to(n):
    count = 1
    while count <= n:
        yield 4
        count += 1

# Using the generator
counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Output: 4
print(next(counter))  # Output: 5
