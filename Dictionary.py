
mydict = {
    "movie":"KGF",
    "actor":"Yash",
    "Language": "Kannada",
    "year" : "2018"
}

print(mydict)

print(mydict["movie"])

print(len(mydict))

print(mydict["year"])

print(mydict.keys())

print(mydict.values())

mydict["collection"] = "500cr"
print(mydict)


for x,y in mydict.items():
    print(x,y)


    
