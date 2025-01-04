def vowel(string):
    vowel = "aeiou"
    count =0
    for i in str(name):
        if i in vowel:
            count+=1
    return count
name =input("Enter a name")
object =vowel(name)
print(f"The number of vowel in the name is :{object}")