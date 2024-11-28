def is_palindrome(word):
    # Convert the word to lowercase to make it case-insensitive
    word = word.lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Test the function
test_word = "Madam"
if is_palindrome(test_word):
    print(f'"{test_word}" is a palindrome.')
else:
    print(f'"{test_word}" is not a palindrome.')
