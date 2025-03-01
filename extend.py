list = [3,5,7,2,5,3,9,6,0,3,4,2,1,7]
new_list = []
threes = []
for i in list:
    if i != 3:
        new_list.append(i)
for i in list:
    if i==3:
        threes.append(i)
new_list.extend(threes)        
print(new_list)




