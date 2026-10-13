l = [1,4,2,3,4,4,4,5,2,3,7,8]

l2 =[]

for i in l:
    if i not in l2:
        l2.append(i)
            
print(l2)


#approach 2 using set but here the original order is not maintained 

l = [1,2,3,4,4,4,5,2,3,7,8]
s = set(l)
            
l = list(s)
print(l)
