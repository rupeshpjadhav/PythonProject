'''
Find second largest number in list.
[10, 20, 4, 45, 99]
'''
#approach 1 using sort function
l = [10, 20, 4, 45, 99]

l.sort

print(l[-2])


# approach 2 using loop and printing the second largest
l2 = [10, 20, 4, 45, 99]
first = second = l2[0]

for num in l2[1:]:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num

print(second)

#approach 3 - sort using loop and then print second largest (bubble sort)
b = [100, 20, 4, 45, 99] 
ln = len(b) #5
for i in range(ln): # no of passes
    for j in range(0,ln-i-1):  # 
        if b[j]>b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
            
print (b)
print (b[-2])