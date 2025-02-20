n = [1,2,3,5,6,7,8,9,10]
flag =0
for i in range(len(n)):
    if n[i+1]-n[i] != 1:
        flag=1
        break
print(f"The missing number is {n[i]+1}")    
        