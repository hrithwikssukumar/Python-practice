list = [2,5,3,8,5,9,4,3]
duplicates = []
for i in list:
    if list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(f"The duplicate elements list: {duplicates}") 