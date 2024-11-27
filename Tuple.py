

mytuple = ("apple","mango",2,3,4,3)

print(mytuple)

print(mytuple[1:4])

mylist = list(mytuple)
mylist[1] = "Banana"
mytuple = tuple(mylist)

print(mytuple)

mylist = list(mytuple)
mylist.append("orange")
mytuple = tuple(mylist)

print(mytuple)

mylist = list(mytuple)
mylist.insert(2,"cherry")
mytuple = tuple(mylist)

print(mytuple)


mylist = list(mytuple)
mylist.remove("apple")
mytuple = tuple(mylist)

print(mytuple)

print(mytuple.count(2))
