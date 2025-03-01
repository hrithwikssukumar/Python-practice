list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
n = 2
for i in list:
    if i%2==0:
        new_list.append(i**n)
        n = n+1
    else:
        new_list.append(i)
print(f"The modified list is : {new_list}")  




def inter_increase(list):
    new_list=[]
    n=2
    for i in list:
        if i%2==0:
            new_list.append(i**n)
            n+=1
        else:
            new_list.append(i)
    return new_list        
            
list = [1,2,3,4,5,6,7,8,9,10]   
result = inter_increase(list)
print(f"The modified list is :{result}")
        