
name = input("Enter the name:")

name = name.replace(" ","").lower()

if name == name[::-1]:
    print(f"The name is palindrome")
else:
    print(f"The name is not palindrome")


def is_palindrome(string):
    
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')




