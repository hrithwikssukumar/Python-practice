list = [1,2,3,4,5,6,7,8,9,10]
new_list =[]
for i in list:
    if i%2==0:
        new_list.append(i*i)
    else:
        new_list.append(i)
print(new_list)





def inter_square(list):
    new_list =[]
    for i in list:
        if i%2==0:
            new_list.append(i*i)
        else:
            new_list.append(i)
    return new_list        
            
            
list = [1,2,3,4,5,6,7,8,9,10]
result = inter_square(list)
print(f"The modified list is :{result}")