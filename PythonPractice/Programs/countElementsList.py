l = [1,2,3,4,4,5,6,7,8]

print(l.count(4)) #get count of specific elements


print(len(l)) # total count of elements

count = 0 # using loop
for i in l[0::]: 
    count = count + 1
print(count)
