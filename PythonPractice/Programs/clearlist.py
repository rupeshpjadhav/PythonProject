l = [1,3,4,5,6,7,2,8]
print(l)
l.clear()
print(l)
 
l = [1,3,4,5,6,7,2,8]
print(l)
for i in l[:]:
    l.remove(i)
print(l)    
