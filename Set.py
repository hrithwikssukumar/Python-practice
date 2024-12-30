

fruits = {"apple","mango","orange"}
colours = {"red","yellow","orange","blue"}

print(fruits)
print(colours)

fruits.add("cherry")
print(fruits)

new = fruits.difference(colours)
print(new)

fruits.remove("mango")
print(fruits)

common = fruits.intersection(colours)
print(common)

union = fruits.union(colours)
print(union)

for i in fruits:
    print(i)

list = ["cherry","Banana"]   
fruits.update(list)
print(fruits)

new1 = fruits.symmetric_difference(colours)
print(new1)


