def pangram(string):
    alpha = 'abcdefhijklmnopqrstuvwxyz'
    string = string.lower()
    for char in alpha:
        if char not in string:
            return f"Not a Pangram"
    return f"It's a Pangram"        
            
sent = input("Enter a sentence: ")
result = pangram(sent)
print(result)